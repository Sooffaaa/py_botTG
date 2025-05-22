import sqlite3
from datetime import datetime


class BotDB:
    def __init__(self, db_file):
        """Инициализация соединения с БД"""
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """Проверяем, есть ли юзер в БД"""
        result = self.cursor.execute("SELECT id FROM users WHERE user_id = ?", (user_id,))
        return bool(result.fetchone())

    def get_user_id(self, user_id):
        """Получаем id юзера в таблице users"""
        result = self.cursor.execute("SELECT id FROM users WHERE user_id = ?", (user_id,))
        user = result.fetchone()
        if user:
            return user[0]
        raise ValueError(f"Пользователь с user_id={user_id} не найден")

    def add_user(self, user_id):
        """Добавляем нового пользователя"""
        self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
        self.conn.commit()

    def add_record(self, user_id, operation, value):
        """Создаем запись о доходе/расходе"""
        self.cursor.execute(
            "INSERT INTO records (users_id, operation, value, date) VALUES (?, ?, ?, ?)",
            (self.get_user_id(user_id), operation, value, datetime.now())
        )
        self.conn.commit()

    def get_records(self, user_id, within="*"):
        """Получаем историю операций за указанный период"""
        user_id = self.get_user_id(user_id)

        if within == "day":
            result = self.cursor.execute("""
                SELECT * FROM records 
                WHERE users_id = ? AND date BETWEEN datetime('now', 'start of day') AND datetime('now', 'localtime') 
                ORDER BY date
            """, (user_id,))
        elif within == "month":
            result = self.cursor.execute("""
                SELECT * FROM records 
                WHERE users_id = ? AND date BETWEEN datetime('now', 'start of month') AND datetime('now', 'localtime') 
                ORDER BY date
            """, (user_id,))
        elif within == "year":
            result = self.cursor.execute("""
                SELECT * FROM records 
                WHERE users_id = ? AND date BETWEEN datetime('now', 'start of year') AND datetime('now', 'localtime') 
                ORDER BY date
            """, (user_id,))
        else:
            result = self.cursor.execute("""
                SELECT * FROM records 
                WHERE users_id = ? 
                ORDER BY date
            """, (user_id,))

        return result.fetchall()

    def close(self):
        """Закрытие соединения"""
        self.conn.close()
