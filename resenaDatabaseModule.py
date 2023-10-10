from dataBaseModule import insert

def guardar_resena(data):
    print(data)
    createResenaSql = ("INSERT INTO resenas (res_contenido, res_valoracion, res_fecha_creacion, res_active, pub_id)"
        f"VALUES ('{data['contenido']}', '{data['valoracion']}', '{data['fecha']}', '{data['active']}', '{data['pubId']}')")
    
    result = insert(createResenaSql)
    print(result)