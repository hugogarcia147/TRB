from dataBaseModule import execute

def get_valorations_by(publicationId):
    rows = execute(f"SELECT * FROM publicacion WHERE pub_id = {publicationId}")
    publications = {
            'title': rows[0][0],
            'image': rows[0][1],
            'id': rows[0][2],
            'description': rows[0][5],
            'valoration': rows[0][6],
            'data': rows[0][7]
        }

    return publications


def get_reviews_by(publicationId):
    rows = execute(f"SELECT * FROM resenas WHERE pub_id = {publicationId}")
    resenas = []

    for row in rows:
        resenas.append(
            {
                'description': row[1],
                'valoration': row[2],
                'date': row[3]
            }
        )

    print(resenas)

    return resenas