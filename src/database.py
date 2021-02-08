import sqlite3
import os

#database class
class DB:
    file = "database.db"

    #initalization
    def __init__(self):
        self.conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), self.file))
        self.cursor = self.conn.cursor()
        self.createStructure()

    #util functions
    def execute(self, query, args = ()):
        try:
            self.cursor.execute(query, args)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
    def fetch(self, query, args = ()):
        try:
            return self.cursor.execute(query, args).fetchall()
        except Exception as e:
            print(e)
            return False

    #generates the db structure if not present
    def createStructure(self):
        self.execute("""CREATE TABLE IF NOT EXISTS points_table(
            property VARCHAR(128) NOT NULL,
            value TEXT NOT NULL,
            PRIMARY KEY (property));""")
    
    def find_points(self, property, default = False):
        product = self.fetch("SELECT value FROM points_table WHERE property = ?", (property,))
        if product != False and len(product) > 0:
            return product[0][0]
        else:
            return default

    def update_points(self, property, value):
        self.execute("UPDATE points_table SET value = ? WHERE property = ?", (property, value))
        if self.cursor.rowcount == 0:
            return self.execute("INSERT INTO points_table (property, value) VALUES (?, ?)", (property, value))
        else:
            return True