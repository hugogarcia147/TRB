from dataBaseModule import insert, execute

def guardar(data):
    createPublicationSql= ("INSERT INTO publicacion (pub_titulo,pub_imagen, mun_id,seccionId,pub_description,pub_valoracion,pub_fecha_creacion) "
        f"VALUES ('{data['title']}', '{data['image']}', {data['town']}, {data['category']}, '{data['description']}', 0, '{data['createdData']}')")
    print(createPublicationSql)
    
    result = insert(createPublicationSql)

    print(result)

def get_publications_by_island(islandId, categoryId):
    get_publications_sql = ("SELECT p.* "
                                "FROM publicacion p "
                                "INNER JOIN municipios m ON m.mun_id = p.mun_id "
                                "INNER JOIN comarcas c ON c.com_id = m.com_id "
                                "INNER JOIN islas i ON i.isl_id = c.isl_id "
                                f"WHERE i.isl_id = {islandId} AND p.seccionId = {categoryId}")
    rows = execute(get_publications_sql)
    publications = list()

    for row in rows:
        publications.append(
            {
                'description': row[5],
                'title': row[0],
                'dataCreate': row[7],
                'valoration': row[6],
                'url': f'/valoration/{row[2]}',
                'image': row[1]
            }
        )
    print(publications)
    
    return publications

def get_publications_by_town(townId, categoryId):
    get_publications_sql = (f"SELECT * FROM publicacion WHERE mun_id = {townId} and seccionId = {categoryId}")
    rows = execute(get_publications_sql)
    publications = list()

    for row in rows:
        publications.append(
            {
                'description': row[5],
                'title': row[0],
                'dataCreate': row[7],
                'valoration': row[6],
                'url': f'/valoration/{row[2]}',
                'image': row[1]
            }
        )
    
    return publications