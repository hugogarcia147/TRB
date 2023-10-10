from dataBaseModule import execute

def get_towns_by(regionId):
    rows = execute(f"select * from municipios WHERE com_id={regionId}")
    towns = []

    for row in rows:
        towns.append(
            {
                "id": row[0],
                "name": row[1],
                "url": f"/municipio/{row[0]}",
            }
        )

    return towns

def get_town_by(townId):
    rows = execute(f"select * from municipios WHERE mun_id={townId}")

    # Comprobar que la colección de rows SIEMPRE TIENE AL MENOS UN ELEMENTO
    # En el caso de que no tenga elementos, devolver un None

    return {
        "id": rows[0][0], #[[1, 'antonio']] --> 1
        "name": rows[0][1] #[[1, 'antonio']] --> antonio
    }