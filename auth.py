# auth.py
from db import get_conn, hash_pwd

def verify_user(uid: str, pwd: str) -> bool:
    """验证工号/密码（明文对比哈希）"""
    h = hash_pwd(pwd)
    with get_conn() as conn:
        cur = conn.execute("SELECT 密码 FROM users WHERE 工号=?", (uid,))
        row = cur.fetchone()
    return bool(row and row[0] == h)

def upsert_user(uid: str, pwd: str):
    """插入或更新用户密码"""
    h = hash_pwd(pwd)
    with get_conn() as conn:
        conn.execute("""
            INSERT INTO users(工号, 密码) VALUES(?, ?)
            ON CONFLICT(工号) DO UPDATE SET 密码=excluded.密码
        """, (uid, h))
        conn.commit()
