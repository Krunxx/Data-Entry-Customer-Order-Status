import sqlite3
from tkinter.messagebox import showerror

#OOP
class CustomerInfoDb:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS tblusers (id INTEGER PRIMARY KEY, CustomerID text, Firstname text, Lastname text, Age text,  OrderStatus text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM tblusers")
        rows = self.cur.fetchall()
        return rows

    def insert(self, CustomerID, Firstname, Lastname, Age, OrderStatus):
        self.cur.execute("INSERT INTO tblusers VALUES (NULL, ?, ?, ?, ?, ?)",
                         (CustomerID, Firstname, Lastname, Age, OrderStatus))
        self.conn.commit()
    
    def remove(self, id):
        self.cur.execute("DELETE FROM tblusers WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, CustomerID, Firstname, Lastname, Age, OrderStatus):
        try:
            self.cur.execute("UPDATE tblusers SET CustomerID = ?, Firstname = ?, Lastname = ?, Age = ?, OrderStatus = ?, WHERE id = ?",
                            (CustomerID, Firstname, Lastname, Age, OrderStatus, id))
            
        except sqlite3.OperationalError as e:
            showerror ("", "Oh no")
        
        finally:
            self.conn.commit()
    
    def __del__(self):
        self.conn.close()