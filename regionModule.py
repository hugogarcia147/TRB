from dataBaseModule import execute

def get_regions_by(islandsId):
    rows = execute(f"select * from comarcas WHERE isl_id={islandsId}")
    regions = list()

    for row in rows:
        regions.append(
            {
                "id": row[0],
                "name": row[1]
            }
        )

    return regions