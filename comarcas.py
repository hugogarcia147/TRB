import sqlite3

conection = sqlite3.connect("../TRB/basededatos/puntuar.db")

cursor = conection.cursor()
cursor.execute("select * from comarcas")
rows = cursor.fetchall()
for row in rows:
    print(row)

conection.close()
