# validate_model.py

import sys
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# —— 中文字体设置 —— #
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

def load_and_prepare(csv_path):
    df = pd.read_csv(csv_path)
    df = df.dropna(subset=['VB']).reset_index(drop=True)
    X = df[['time','DOC','feed',
            'smcAC','smcDC',
            'vib_table','vib_spindle',
            'AE_table','AE_spindle']]
    mats = pd.get_dummies(df['material'], prefix='mat')
    for col in ['mat_1','mat_2']:
        if col not in mats:
            mats[col] = 0
    mats = mats[['mat_1','mat_2']]
    X = pd.concat([X, mats], axis=1)
    y = df['VB'].values
    return train_test_split(X, y, test_size=0.2, random_state=42)

def main():
    if len(sys.argv) != 3:
        print("用法: python validate_model.py <mill.csv> <wear_model.pkl>")
        sys.exit(1)

    csv_path, model_path = sys.argv[1], sys.argv[2]

    # 加载模型
    model = joblib.load(model_path)
    print(f"已加载模型: {model_path}")

    # 加载并切分数据
    X_train, X_test, y_train, y_test = load_and_prepare(csv_path)
    print(f"数据集大小: 训练 {len(X_train)} 条, 测试 {len(X_test)} 条")

    # 预测
    y_pred = model.predict(X_test)

    # 评估指标
    mse  = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae  = mean_absolute_error(y_test, y_pred)
    r2   = r2_score(y_test, y_pred)
    print("测试集评估指标:")
    print(f"  RMSE = {rmse:.4f}")
    print(f"  MAE  = {mae:.4f}")
    print(f"  R²   = {r2:.4f}")

    # 散点图：预测 vs 实际
    plt.figure(figsize=(6,6))
    plt.scatter(y_test, y_pred, alpha=0.7)
    mn, mx = min(min(y_test), min(y_pred)), max(max(y_test), max(y_pred))
    plt.plot([mn, mx], [mn, mx], 'r--', linewidth=1)
    plt.xlabel("实际磨损 VB")
    plt.ylabel("预测磨损 VB")
    plt.title("预测 vs 实际")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("pred_vs_actual.png")
    plt.show()

    # 残差分布直方图
    residuals = y_test - y_pred
    plt.figure(figsize=(6,4))
    plt.hist(residuals, bins=30, edgecolor='black')
    plt.xlabel("残差 (实际 - 预测)")
    plt.title("残差分布")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("residuals_hist.png")
    plt.show()

    # 时序对比图
    plt.figure(figsize=(8,4))
    plt.plot(range(len(y_test)), y_test, label="实际", marker='o')
    plt.plot(range(len(y_test)), y_pred, label="预测", marker='x')
    plt.xlabel("测试样本索引")
    plt.ylabel("磨损 VB")
    plt.title("测试样本 实际 vs 预测 磨损")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("timeseries_compare.png")
    plt.show()

if __name__ == "__main__":
    main()
