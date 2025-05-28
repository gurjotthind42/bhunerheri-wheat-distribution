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
    "fps_id": row[0],
    "alloted": row[1],  # ← changed from allocation to alloted for frontend compatibility
    "received": row[2],
    "issued": row[3],
    "cb": row[4],
    "yesterday_issued": row[5] or 0,
    "today_distribution": today_dist,
    "distribution_percentage": round(dist_pct, 2),
    "updated_on": row[6]
})

        return result

init_db()
