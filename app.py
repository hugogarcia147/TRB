from flask import Flask, render_template, request
from translationsModule import obtener_palabras_segun_idioma
from cardsModule import get_cards_islands_by, get_card_island_by
from idiomasModule import get_all_idiomas
from sessionModule import get_language
from sectionsModule import get_sections_by
from translationsModule import obtener_palabras_segun_idioma
from regionModule import get_regions_by
from islandsModule import get_islands_by
from townsModule import get_towns_by, get_town_by
from publicationServiceModule import guardar_publicacion
from publicationDatabaseModule import get_publications_by_island, get_publications_by_town
from valorationsModule import get_valorations_by, get_reviews_by
from resenaServiceModule import guardar_valoraciones


app = Flask(__name__)

def createAppContext():
    pageContext = PageContext()
    pageContext.session = get_language()
    pageContext.idiomas = get_all_idiomas()
    pageContext.translations = obtener_palabras_segun_idioma(pageContext.session)

    return pageContext

def render(
        page_template, # Nombre de la plantilla a usar dentro de la carpeta /templates 
        pageContext, # Objeto con la información básica del usuario (lenguaje) y traducciones
        pageData # Información del cuerpo de la página como un objeto
):

    if page_template == 'index.html':
        menu = None
    else:
        menu = []


    return render_template(
        page_template,
        translations = pageContext.translations,
        idiomas=pageContext.idiomas,
        session=pageContext.session,
        menu = menu,
        data = pageData
    )


@app.route('/municipio/<townId>')
def get_publication_by(townId):
    context = createAppContext()

    return render(
        'municipios.html',
        context,
        {
            'menu': get_islands_by(context.session),
            'town': get_town_by(townId),
            'sections': get_sections_by(context.session),
            'publications': get_publications_by_town(townId, 1)
        }
    )

@app.route('/valoration/<publicationId>')
def get_valoration_by(publicationId):
    context = createAppContext()

    return render(
        'valoraciones.html',
        context,
        {
            'publicacionId': publicationId,
            'valorations': get_valorations_by(publicationId),
            'resenas' : get_reviews_by(publicationId)
        }
    )


@app.route('/publicar')
def publicar():
    context = createAppContext()

    return render(
        'crearPublicacion.html',
        context,
        {
            'menu': get_islands_by(context.session),
            'island': get_islands_by(context.session),
            'categoria': get_sections_by(context.session)
        }
    )


# @app.route('/publicaciones')
# def publicaciones():
#     context = createAppContext()

#     return render(
#         'publicaciones.html',
#         context,
#         {
#             'menu': get_islands_by(context.session)
#         }
#     )



@app.route('/')
def home():
    context = createAppContext()

    return render(
        'index.html',
        context,
        {
            'cards': get_cards_islands_by(context.session)
        }
    )

@app.route('/isla/<islandId>')
def island(islandId):
    context = createAppContext()
    island_card = get_card_island_by(islandId, context.session)

    return render(
        'islas.html',
        context,
        {
            'sections': get_sections_by(context.session),
            'island': island_card,
            'menu': get_islands_by(context.session),
            'publications': get_publications_by_island(islandId, 1),
            'islandId': islandId
        }
    )

@app.route('/explore')
def selectores():
    context = createAppContext()

    return render(
        'selectores.html',
        context,
        {
            'menu': get_islands_by(context.session),
            'island': get_islands_by(context.session)
        }
    )



@app.route('/login')
def login():
    context = createAppContext()    

    return render(
        'login.html',
        context,
        {
            'menu': get_islands_by(context.session)
        }
    )

@app.route('/registrarse')
def registrarse():
    context = createAppContext()

    return render(
        'registrarse.html',
        context,
        {
            'menu': get_islands_by(context.session),
        }
    )



@app.route('/publicacion/<islandId>/<categoryId>')
def get_publication_by_island(islandId, categoryId):
    publication = get_publications_by_island(islandId, categoryId)
    return publication

@app.route('/municipio/<townId>/<categoryId>')
def get_publication_by_town(townId, categoryId):
    publication = get_publications_by_town(townId, categoryId)
    
    return publication


@app.route('/isla/<islandId>/comarcas')
def getRegionsByIsland(islandId):
    # return [
    #     {
    #         'id': 1,
    #         'name': 'Comarca name'
    #     }
    # ]

    return get_regions_by(islandId) 

@app.route('/comarca/<regionId>/municipios')
def getTownsByRegionId(regionId):
    towns = get_towns_by(regionId)
    return towns

@app.route('/publicacion/crear', methods = ['POST'])
def createPublication():
    guardar_publicacion(request.json)
    return "Created", 201

@app.route('/valoration/crear', methods = ['POST'])
def createValoration():
    guardar_valoraciones(request.json)
    return "Created", 201


class PageContext:
    session: 1
    translations: {}
    idiomas: [] 