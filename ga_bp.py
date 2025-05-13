# ga_bp.py
import numpy as np
import pandas as pd
import random
import math
import joblib
import matplotlib.pyplot as plt
import matplotlib

# —— 中文字体设置 —— #
matplotlib.rcParams['font.sans-serif'] = ['SimHei']      # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus'] = False        # 正确显示负号

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score

def load_and_prepare(csv_path):
    df = pd.read_csv(csv_path)
    df = df.dropna(subset=['VB']).reset_index(drop=True)
    X = df[['time','DOC','feed','smcAC','smcDC','vib_table','vib_spindle','AE_table','AE_spindle']]
    mat_dummies = pd.get_dummies(df['material'], prefix='mat')
    for col in ['mat_1','mat_2']:
        if col not in mat_dummies:
            mat_dummies[col] = 0
    mat_dummies = mat_dummies[['mat_1','mat_2']]
    X = pd.concat([X, mat_dummies], axis=1)
    y = df['VB'].values
    return train_test_split(X, y, test_size=0.2, random_state=42)

def evaluate_individual(ind, X, y):
    hidden, lr, alpha = ind
    model = Pipeline([
        ('scaler', StandardScaler()),
        ('mlp', MLPRegressor(
            hidden_layer_sizes=(hidden,),
            learning_rate_init=lr,
            alpha=alpha,
            max_iter=500,
            random_state=42
        ))
    ])
    scores = cross_val_score(model, X, y, cv=3, scoring='neg_mean_squared_error')
    return -scores.mean()

def init_population(size):
    pop = []
    for _ in range(size):
        hidden = random.randint(5, 100)
        lr     = 10 ** random.uniform(-5, -1)
        alpha  = 10 ** random.uniform(-6, -2)
        pop.append([hidden, lr, alpha])
    return pop

def crossover(p1, p2):
    return [
        p2[0] if random.random() < 0.5 else p1[0],
        (p1[1] + p2[1]) / 2,
        (p1[2] + p2[2]) / 2
    ]

def mutate(ind, mut_rate=0.2):
    if random.random() < mut_rate:
        ind[0] = random.randint(5, 100)
    if random.random() < mut_rate:
        ind[1] *= 10 ** random.uniform(-0.5, 0.5)
        ind[1] = min(max(ind[1], 1e-5), 1e-1)
    if random.random() < mut_rate:
        ind[2] *= 10 ** random.uniform(-0.5, 0.5)
        ind[2] = min(max(ind[2], 1e-6), 1e-2)
    return ind

def ga_optimize(X, y, pop_size=30, generations=100):
    pop = init_population(pop_size)
    history = []
    for gen in range(generations):
        fitness = [evaluate_individual(ind, X, y) for ind in pop]
        best = min(fitness)
        history.append(best)
        idx = np.argsort(fitness)
        survivors = [pop[i] for i in idx[:pop_size//2]]
        children = []
        while len(survivors) + len(children) < pop_size:
            p1, p2 = random.sample(survivors, 2)
            children.append(mutate(crossover(p1, p2)))
        pop = survivors + children
        print(f"Gen {gen+1}/{generations}: Best MSE = {best:.4f}")
    best_ind = min(pop, key=lambda ind: evaluate_individual(ind, X, y))
    return (*best_ind, history)

def train_and_evaluate(csv_path):
    X_train, X_test, y_train, y_test = load_and_prepare(csv_path)
    print("开始遗传算法 + BP 优化…")
    best_h, best_lr, best_alpha, history = ga_optimize(X_train, y_train)
    print(f"最优参数 → hidden={best_h}, lr={best_lr:.5f}, alpha={best_alpha:.6f}")

    # 绘制迭代曲线
    plt.figure()
    plt.plot(range(1, len(history)+1), history, marker='o')
    plt.xlabel("迭代代数")
    plt.ylabel("最优 MSE")
    plt.title("遗传算法迭代最优 MSE 变化")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 最终模型训练
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('mlp', MLPRegressor(
            hidden_layer_sizes=(best_h,),
            learning_rate_init=best_lr,
            alpha=best_alpha,
            max_iter=1000,
            random_state=42
        ))
    ])
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = math.sqrt(mse)
    r2   = r2_score(y_test, y_pred)
    print(f"测试集 RMSE={rmse:.4f}, R²={r2:.4f}")

    # 保存模型
    joblib.dump(pipeline, "wear_model.pkl")
    print("模型已保存为 wear_model.pkl")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("用法: python ga_bp.py mill.csv")
    else:
        train_and_evaluate(sys.argv[1])
