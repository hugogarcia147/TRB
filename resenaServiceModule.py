from resenaDatabaseModule import guardar_resena
from fechaModule import fechaPublicacion

def guardar_valoraciones(data):
    print(data)
    guardar_resena(
        {
            "contenido": data['placeDescription'],
            "valoracion": data['placeValoration'],
            "fecha": fechaPublicacion(),
            "active": 1,
            "pubId": data['placePublicationId']
        }
    )