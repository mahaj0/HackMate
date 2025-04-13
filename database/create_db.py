# create_db.py
import sqlite3

conn = sqlite3.connect("hackmate.db")
cursor = conn.cursor()

# Create a users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database and users table created successfully.")
