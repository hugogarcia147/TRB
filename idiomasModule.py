from dataBaseModule import execute

def get_all_idiomas():
    rows = execute("select * from idiomas")
    idiomas = list()

    for row in rows:
        idioma = {
            "id": row[0],
            "name": row[1],
            "iso": row[2]
        }

        idiomas.append(idioma)
    return idiomas