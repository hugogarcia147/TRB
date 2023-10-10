from publicationDatabaseModule import guardar
from fechaModule import fechaPublicacion
import random

def guardar_publicacion(data):
    guardar(
        {
            'title': data["placeName"],
            'island': data["placeIsland"],
            'town': data["placeTown"],
            'description': data["placeDescription"],
            'category': data["placeCategory"],
            'createdData': fechaPublicacion(),
            'image': fotoRandom(data["placeCategory"])
        }
    )


def fotoRandom(categoriaId):
    numero_aleatorio = random.randint(1,4)
    print(numero_aleatorio)
    return "seccion-"+str(categoriaId)+"-"+str(numero_aleatorio)