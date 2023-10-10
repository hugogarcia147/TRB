from dataBaseModule import execute

def get_sections():
    rows = execute("select * from seccion")
    sections = list()

    for row in rows:
        sections.append(
            {
                "id": row[0],
                "name": row[1]
            }
        )

    return sections

def get_sections_by(idiomaId):
    rows = execute(f"select * from seccionIdioma WHERE idiomaId = {idiomaId}")
    sections = list()

    for row in rows:
        sections.append(
            {
                "id": row[2],
                "name": row[1]
            }
        )
    return sections


"""
def get_sections():
    sections = [
        {
            'name': 'playas'
        },
        {
            'name': 'montañas'
        },
        {
            'name': 'pueblos'
        },
        {
            'name': 'ciudades'
        }
    ]

    return sections
"""