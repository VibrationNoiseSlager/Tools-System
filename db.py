# db.py
import hashlib
import sqlite3
import pathlib
import textwrap

ROOT    = pathlib.Path(__file__).parent
DB_FILE = ROOT / "Tool_system_data_base.db"

# 所有刀具表 DDL 按照 UI 中字段定义
DDL_MAP = {
    "drill_tools": textwrap.dedent("""
        CREATE TABLE IF NOT EXISTS drill_tools(
            刀具编号 TEXT PRIMARY KEY, 刀具型号 TEXT NOT NULL,
            刀具属性 TEXT, 生产商 TEXT, 工序类型 TEXT,
            刀柄形状 TEXT, 推荐钻深 INTEGER, 顶角角度 INTEGER,
            直径 INTEGER, 冷却方式 TEXT, 刀具总长 INTEGER,
            刃长 INTEGER, 排屑槽长度 INTEGER, 刀具材料 TEXT,
            适合加工材料 TEXT, 库存位置 TEXT, 入库人 TEXT,
            入库时间 TEXT, 库存状态 TEXT, 借用人 TEXT,
            借用时间 TEXT, 归还时间 TEXT, 刀具状况 TEXT,
            使用次数 INTEGER
        );"""),
    "indexable_mill_tools": textwrap.dedent("""
        CREATE TABLE IF NOT EXISTS indexable_mill_tools(
            刀具编号 TEXT PRIMARY KEY, 刀具型号 TEXT NOT NULL,
            刀具属性 TEXT, 生产商 TEXT, 刀片形状 TEXT,
            主切削刃后角 INTEGER, 有无孔 TEXT, 有无断屑槽 TEXT,
            切削刃长度 INTEGER, 修光刃主偏角 INTEGER, 修光刃后角 INTEGER,
            刃倾角 INTEGER, 切削刃倒角 INTEGER, 刀具材料 TEXT,
            适合加工材料 TEXT, 库存位置 TEXT, 入库人 TEXT,
            入库时间 TEXT, 库存状态 TEXT, 借用人 TEXT,
            借用时间 TEXT, 归还时间 TEXT, 刀具状况 TEXT,
            使用次数 INTEGER
        );"""),
    "solid_mill_tools": textwrap.dedent("""
        CREATE TABLE IF NOT EXISTS solid_mill_tools(
            刀具编号 TEXT PRIMARY KEY, 刀具型号 TEXT NOT NULL,
            刀具属性 TEXT, 生产商 TEXT, 刃数 INTEGER,
            刀具类型 TEXT, 长度类型 TEXT, 刀柄结构 TEXT,
            直径 INTEGER, 螺旋角 INTEGER, 刃径公差 INTEGER,
            刀具材料 TEXT, 适合加工材料 TEXT, 库存位置 TEXT,
            入库人 TEXT, 入库时间 TEXT, 库存状态 TEXT,
            借用人 TEXT, 借用时间 TEXT, 归还时间 TEXT,
            刀具状态 TEXT, 使用次数 INTEGER
        );"""),
    "turning_inserts": textwrap.dedent("""
        CREATE TABLE IF NOT EXISTS turning_inserts(
            刀具编号 TEXT PRIMARY KEY, 刀具型号 TEXT NOT NULL,
            刀具属性 TEXT, 生产商 TEXT, 刀片形状 TEXT,
            刀片后角 INTEGER, 有无孔 TEXT, 刀片公差 TEXT,
            有无断屑槽 TEXT, 切削刃长度 INTEGER, 刀片厚度 INTEGER,
            刀尖圆弧半径 INTEGER, 刀口形状 TEXT, 切削方向 TEXT,
            刀具材料 TEXT, 适合加工材料 TEXT, 库存位置 TEXT,
            入库人 TEXT, 入库时间 TEXT, 库存状态 TEXT,
            借用人 TEXT, 借用时间 TEXT, 归还时间 TEXT,
            刀具状态 TEXT, 使用次数 INTEGER
        );""")
}

def init_all_tables():
    """初始化 users 表和 4 张刀具表"""
    with sqlite3.connect(DB_FILE) as conn:
        # 用户表
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users(
                工号 TEXT PRIMARY KEY,
                密码 TEXT NOT NULL
            );
        """)
        # 刀具表
        for ddl in DDL_MAP.values():
            conn.executescript(ddl)
        conn.commit()

def get_conn():
    """返回 sqlite3.Connection"""
    return sqlite3.connect(DB_FILE)

def hash_pwd(pwd: str, salt: str = "g!8$") -> str:
    """SHA-256 + 简单盐"""
    return hashlib.sha256((pwd + salt).encode()).hexdigest()
