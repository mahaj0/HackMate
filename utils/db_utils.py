# db_utils.py (SQLite version)
import sqlite3
import hashlib

DB_PATH = "hackmate.db"  # or wherever your .db file is saved

def get_connection():
    return sqlite3.connect(DB_PATH)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, email, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    if cursor.fetchone():
        return False, "Email already registered"

    hashed = hash_password(password)
    cursor.execute(
        "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
        (username, email, hashed)
    )
    conn.commit()
    conn.close()
    return True, "User registered successfully"

def verify_user(email, password):
    conn = get_connection()
    cursor = conn.cursor()
    hashed = hash_password(password)
    cursor.execute(
        "SELECT * FROM users WHERE email = ? AND password_hash = ?",
        (email, hashed)
    )
    result = cursor.fetchone()
    conn.close()
    return result is not None
