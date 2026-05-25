import sqlite3

conn = sqlite3.connect(
    "employees.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS employees (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL

)

""")

conn.commit()