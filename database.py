import sqlite3
import os

class thing:
    file = "../database.db"

    def __init__(self):
        self.conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), self.file))
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.createStructure()

    def execute(self, query, args = ()):
        try:
            self.cursor.execute(query, args)
            self.conn.commit()
            return True
        except Exception as x:
            print(x)
            return False

    def fetch(self, query, args = ()):
        try:
            return self.cursor.execute(query, args).fetchall()
        except Exception as x:
            print(x)
            return False

    def create_structure(self):
        self.execute("""CREATE TABLE IF NOT EXISTS points_table (
            user_id VARCHAR(18) NOT NULL,
            points INTEGER NOT NULL,
            PRIMARY KEY (user_id));""")
    
    def find_points(self, user_id, default = False):
        product = self.fetch("SELECT points FROM points_table WHERE user_id = ?", (user_id,))
        if product != False and len(product) > 0:
            return product[0]["points"]
        else:
            return default

    def update_points(self, user_id, points):
        self.execute("UPDATE points_table SET points = ? WHERE user_id = ?", (points, user_id))
        if self.cursor.rowcount == 0:
            return self.execute("INSERT INTO points_table (user_id, points) VALUES (?, ?)", (user_id, points))
        else:
            return True