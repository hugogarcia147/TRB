from dataBaseModule import execute

def get_all_islands():
    rows = execute("select * from islas")
    islands = list()

    for row in rows:
        islands.append(
            {
                "id": row[0],
                "name": row[1]
            }
        )

    return islands

def get_islands_by(idiomaId):
    rows = execute(f"select * from islandCard WHERE idiomaId = {idiomaId}")
    islands = list()

    for row in rows:
        islands.append(
            {
                "title": row[3],
                "id": row[1],
                "url": f"/isla/{row[1]}"
            }
        )
    return islands