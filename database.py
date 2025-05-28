import sqlite3
from datetime import datetime

DB_FILE = "fps.db"

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS wheat (
                fps_id TEXT PRIMARY KEY,
                allocation REAL,
                received REAL,
                issued REAL,
                cb REAL,
                yesterday_issued REAL,
                updated_at TEXT
            )
        ''')

def save_fps_entry(data):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO wheat (fps_id, allocation, received, issued, cb, updated_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            data["fps_id"],
            data["allocation"],
            data["received"],
            data["issued"],
            data["cb"],
            datetime.now().isoformat()
        ))
        conn.commit()

def update_yesterday():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute('UPDATE wheat SET yesterday_issued = issued')

def get_wheat_data():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        rows = cursor.execute('SELECT * FROM wheat').fetchall()
        result = []
        for row in rows:
            today_dist = row[3] - (row[5] or 0)
            dist_pct = (row[3] / row[1] * 100) if row[1] else 0
            result.append({
                "fps_id": "104800100001",
            "alloted": "250",
            "received": "200",
            "issued": "180",
            "yesterday_issued": "170",
            "today_distribution": "10",
            "cb": "20",
            "updated_on": "2025-05-28T12:00:00"
            })
        return result

init_db()
