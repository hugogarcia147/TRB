import sqlite3

def execute(query) -> list:
    connction = sqlite3.connect("basededatos/puntuar.db")
    cursor = connction.cursor()
    cursor.execute(query)
    
    datas = cursor.fetchall()
    
    connction.close()

    return datas

def insert(query):
    connction = sqlite3.connect("basededatos/puntuar.db")
    cursor = connction.cursor()
    cursor.execute(query)
    
    connction.commit()
    connction.close()

    return cursor.lastrowid