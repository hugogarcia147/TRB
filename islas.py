import sqlite3

def execute_command(command):
    connection = sqlite3.connect("../TRB/basededatos/puntuar.db")
    cursor = connection.cursor()
    
    cursor.execute(command)
    result = cursor.fetchall()

    connection.close()

    return result


# result = execute_command("select * from islas")

# print(result)

# result = execute_command("select * from islas where isl_id = 1")

# print(result)

result = execute_command("select * from islas isl inner join comarcas com on com.isl_id = isl.isl_id inner join municipios mun on mun.com_id = com.com_id where isl.isl_id = 1")

for row in result:
    print(row)






# numero_isla = input("Elige un numero del uno al cuatro: ")
# if not numero_isla.isnumeric():
#     print("Valor incorrecto")
#     exit()

# result = execute_command(f"select * from comarcas where isl_id = {numero_isla}")
# if len(result) == 0:
#     print("Isla incorrecta")
#     exit()
# print(result)

# numero_comarca = input("Elige un numero del uno al siete: ")
# if not numero_comarca.isnumeric():
#     print("Valor incorrecto")
#     exit()
# result = execute_command(f"select * from municipios where com_id = {numero_comarca}")
# print(result)
