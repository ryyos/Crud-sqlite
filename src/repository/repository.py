import sqlite3
from typing import Dict

class Repository:
    def __init__(self) -> None:
        ...

    def search_by_username(self, username: str) -> Dict[str, any]:
        conn = sqlite3.connect('src/database/database.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        if row:
            return {
                'id': row[0],
                'name': row[1],
                'username': row[2],
                'ages': row[3]
            }
        else:
            conn.close()
            return None

    def add_data(self, name: str, username: str, ages: str) -> None:
        conn = sqlite3.connect('src/database/database.sqlite')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, username, ages) VALUES (?, ?, ?)", (name, username, ages))
        conn.commit()
        conn.close()

    def update_data(self, name: str, username: str, ages: str) -> None:
        conn = sqlite3.connect('src/database/database.sqlite')
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET name = ?, ages = ? WHERE username = ?", (name, ages, username))
        conn.commit()
        conn.close()

    def delete_data(self, username: str) -> None:
        conn = sqlite3.connect('src/database/database.sqlite')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        conn.commit()
        conn.close()
