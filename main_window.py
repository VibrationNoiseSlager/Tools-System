# main_window.py

from PySide6.QtCore        import Qt, QThread, Signal, QPointF
from PySide6.QtGui         import QPainter, QColor, QPen, QBrush
from PySide6.QtWidgets     import (
    QMainWindow, QFileDialog, QMessageBox, QHeaderView, QGraphicsSimpleTextItem
)
from PySide6.QtCharts      import QChart, QPieSeries, QLineSeries, QValueAxis
import PySide6.QtSql        as QtSql
import pandas as pd
import joblib

from Interface_module      import Ui_Form
from db                    import get_conn, DB_FILE

MODEL_FILE = "wear_model.pkl"


class PredictWorker(QThread):
    progress = Signal(int)
    finished = Signal(list, list)

    def __init__(self, csv_path):
        super().__init__()
        self.csv_path = csv_path

    def run(self):
        # 1) 加载模型
        self.progress.emit(5)
        model = joblib.load(MODEL_FILE)
        self.progress.emit(20)

        # 2) 读取 CSV 并预处理
        df = pd.read_csv(self.csv_path)
        feat_cols = [
            'time', 'DOC', 'feed',
            'smcAC', 'smcDC',
            'vib_table', 'vib_spindle',
            'AE_table', 'AE_spindle'
        ]
        X = df[feat_cols]

        # 独热编码 material 列
        mats = pd.get_dummies(df['material'], prefix='mat')
        for col in ['mat_1', 'mat_2']:
            if col not in mats:
                mats[col] = 0
        mats = mats[['mat_1', 'mat_2']]
        X = pd.concat([X, mats], axis=1)
        self.progress.emit(50)

        # 3) 预测
        y_pred = model.predict(X)
        self.progress.emit(90)

        # 4) 发射结果
        self.finished.emit(list(df.index), y_pred.tolist())
        self.progress.emit(100)


class MainWindow(QMainWindow):
    TABLE_MAP = {
        0: "drill_tools",
        1: "indexable_mill_tools",
        2: "solid_mill_tools",
        3: "turning_inserts"
    }
    CHART_MAP = {
        "drill_tools":          "Chart_drill",
        "indexable_mill_tools": "Chart_indexmill",
        "solid_mill_tools":     "chart_solidmill",
        "turning_inserts":      "Chart_turninsert"
    }

    def __init__(self, user: str):
        super().__init__()
        self.user = user
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 打开 SQLite 数据库
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE", "tools_conn")
        db.setDatabaseName(str(DB_FILE))
        if not db.open():
            QMessageBox.critical(self, "数据库错误", db.lastError().text())

        # 界面切换按钮
        self.ui.Main_interface_button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Main_interface))
        self.ui.Visual_interface_button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Visual_interface))
        self.ui.Testing_interface_button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Testing_interface))

        # 刀具库管理模块
        self.model = None
        self.ui.Tool_category_comboBox.currentIndexChanged.connect(self.load_table)
        self.ui.Tool_information_search_button.clicked.connect(self.search_tool)
        self.ui.Tool_information_delete.clicked.connect(self.delete_selected)
        self.ui.Tool_information_enty.clicked.connect(self.insert_row)
        self.load_table(0)

        # 可视化模块
        self.ui.Image_refresh_button.clicked.connect(self.refresh_charts)
        self.refresh_charts()

        # 磨损检测模块
        self.csv_path = ""
        self.ui.Data_import_button.clicked.connect(self.import_csv)
        try:
            self.ui.Start_data_analysis_button.clicked.disconnect()
        except TypeError:
            # 如果没有需要断开的信号连接，就忽略
            pass
        self.ui.Start_data_analysis_button.clicked.connect(self.start_predict)

    # —— 刀具数据库操作 —— #
    def load_table(self, idx: int):
        table = self.TABLE_MAP[idx]
        db = QtSql.QSqlDatabase.database("tools_conn")
        self.model = QtSql.QSqlTableModel(self, db)
        self.model.setTable(table)
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        tv = self.ui.Tool_information_view
        tv.setModel(self.model)
        tv.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def search_tool(self):
        txt = self.ui.Input_tool_information.text().strip()
        filt = f"刀具编号 LIKE '%{txt}%' OR 刀具型号 LIKE '%{txt}%'" if txt else ""
        self.model.setFilter(filt)
        self.model.select()

    def delete_selected(self):
        idx = self.ui.Tool_information_view.currentIndex()
        if idx.isValid():
            self.model.removeRow(idx.row())
            self.model.submitAll()

    def insert_row(self):
        self.model.insertRow(self.model.rowCount())

    # —— 饼图可视化 —— #
    def refresh_charts(self):
        conn = get_conn()
        cur = conn.cursor()
        for table, attr in self.CHART_MAP.items():
            col = "刀具状况" if table in ("drill_tools", "indexable_mill_tools") else "刀具状态"
            counts = {s: 0 for s in ("新", "良好", "差")}
            for s in counts:
                cur.execute(f"SELECT COUNT(*) FROM {table} WHERE {col}=?", (s,))
                counts[s] = cur.fetchone()[0]
            view = getattr(self.ui, attr)
            self._draw_pie(view, counts, table)
        conn.close()

    @staticmethod
    def _draw_pie(view, counts, title):
        series = QPieSeries()
        total = sum(counts.values())
        if total == 0:
            sl = series.append("无数据", 1)
            sl.setBrush(Qt.lightGray)
            sl.setLabelVisible(True)
        else:
            cmap = {"新": "#2ecc71", "良好": "#f1c40f", "差": "#e74c3c"}
            for k, v in counts.items():
                sl = series.append(f"{k} {v}", v)
                sl.setBrush(QColor(cmap[k]))
                sl.setLabelVisible(True)
                if k == "差" and v:
                    sl.setExploded(True)
        chart = QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setTitle(f"{title} — 刀具状况占比")
        chart.legend().setAlignment(Qt.AlignRight)
        view.setRenderHint(QPainter.Antialiasing)
        view.setChart(chart)

    # —— 导入 CSV —— #
    def import_csv(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "选择 CSV 文件", "", "CSV Files (*.csv)"
        )
        if path:
            self.csv_path = path
            self.ui.File_path_display.setText(path)

    # —— 启动预测线程 —— #
    def start_predict(self):
        if not self.csv_path:
            QMessageBox.warning(self, "提示", "请先导入 CSV 文件")
            return
        self.ui.Data_analysis_loading_progress_bar.setValue(0)
        self.worker = PredictWorker(self.csv_path)
        self.worker.progress.connect(self.ui.Data_analysis_loading_progress_bar.setValue)
        self.worker.finished.connect(self.show_predict)
        self.worker.start()

    # —— 显示预测结果 —— #
    def show_predict(self, x, y_pred):
        # 计算预测最大磨损值
        max_pred = float(max(y_pred))

        # 创建图表
        chart = QChart()

        # 预测磨损曲线
        series_pred = QLineSeries()
        series_pred.setName("预测磨损")
        for xi, yi in zip(x, y_pred):
            series_pred.append(float(xi), float(yi))
        series_pred.setPen(QPen(QColor("#007acc"), 2))
        chart.addSeries(series_pred)

        # 预测最大磨损量横线
        series_max = QLineSeries()
        series_max.setName("预测最大磨损量")
        series_max.append(min(x), max_pred)
        series_max.append(max(x), max_pred)
        series_max.setPen(QPen(QColor("#e74c3c"), 2, Qt.DashLine))
        chart.addSeries(series_max)

        # 坐标轴设置
        axisX = QValueAxis()
        axisX.setTitleText("运行次数 (time)")
        axisX.setLabelFormat("%d")
        axisX.setRange(min(x), max(x))

        axisY = QValueAxis()
        axisY.setTitleText("磨损量 VB")
        axisY.setLabelFormat("%.2f")
        axisY.setRange(0, max_pred * 1.1)

        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)
        series_pred.attachAxis(axisX); series_pred.attachAxis(axisY)
        series_max.attachAxis(axisX); series_max.attachAxis(axisY)

        # 美化图表
        chart.setTitle("刀具磨损预测与预测最大磨损量")
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignRight)

        # 在 QChartView 中显示
        view = self.ui.Data_analysis_result_presentation
        view.setRenderHint(QPainter.Antialiasing)
        view.setChart(chart)

        # 添加最大值标签到 y 轴
        scene = view.scene()
        if scene is None:
            return
        pt_axis = QPointF(min(x), max_pred)
        pos = chart.mapToPosition(pt_axis, series_pred)
        text = QGraphicsSimpleTextItem(f"{max_pred:.2f}")
        text.setBrush(QBrush(QColor("#e74c3c")))
        bounds = text.boundingRect()
        text.setPos(pos.x() - bounds.width() - 5, pos.y() - bounds.height() / 2)
        scene.addItem(text)
