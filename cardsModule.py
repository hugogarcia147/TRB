from dataBaseModule import execute

def get_cards_islands_by(idiomaId):
    rows = execute(f"select * from islandCard WHERE idiomaId = {idiomaId}")
    islands = list()

    for row in rows:
        islands.append(
            {
                "url": f"/isla/{row[1]}", 
                "image": row[2], 
                "title": row[3],
                "description": row[4]
            }
        )
    return islands


def get_card_island_by(islandId,idiomaId):
    rows = execute(f"select * from islandCard WHERE idiomaId = {idiomaId} and isl_id = {islandId}")

    if len(rows) == 0:
        return None
    
    row = rows[0]

    return {
        "url": f"/isla/{row[1]}", 
        "image": row[2], 
        "title": row[3],
        "description": row[4]
    }



# def get_islands_carts(translations):
#     islas = get_all_islands()
#     for isla in islas:
#         cards.append({})

# def cards():
#     cards = [
#             {
#                 'name': 'Mallorca',
#                 'description': 'Test',
#                 'image': 'mallorca.jpeg',
#                 'id' : 'isla.1'
#             },
#             {
#                 'name': 'Menorca',
#                 'description': 'Test',
#                 'image': 'menorca.jpeg',
#                 'id' : 'isla.2'
#             },
#             {
#                 'name': 'Ibiza',
#                 'description': 'Test',
#                 'image' : 'ibiza.jpeg',
#                 'id' : 'isla.4'
#             },
#             {
#                 'name': 'Formentera',
#                 'description': 'Test',
#                 'image' : 'formentera.jpeg',
#                 'id' : 'isla.3'
#             }
#     ]
#     return cards
# """