from dataBaseModule import execute

def obtener_palabras_segun_idioma(idioma_id):

    datas = execute(f"select * from traducciones where idiomaId = {idioma_id}")
    
    traducciones = {}
    for row in datas:
        # diccionario = { "key": 'value' }
        # Acceso a diccionario => diccionario["key"]
        # Creación de clave => diccionario["key"] = 'valor que quiera'
        # Clave => row[2] (clave en base de datos)
        # Valor => row[3] (valor en base datos)
        traducciones[row[2]] = row[3]
    return traducciones

"""
def translations():
    translations = {
        # Cabecera
        'es-es': 'Español',
        'en-en': 'Inglés',
        'languages': 'Idiomas',
        'spanish': 'Español',
        'english': 'Inglés',
        'createNewUser': 'Regístrate',
        'profile' : 'Perfil',
        'login' : 'Iniciar Sesión',
        # Formulario de registro
        'signUp' : 'Registrarse',
        'signUpWithGoogle' : 'Registrarse con google',
        'or' : 'O',
        'name' : 'Nombre',
        'username' : 'Nombre de usuario',
        'password' : 'Contraseña',
        'iAcceptTheTermsAndConditionsAndTheLegalNotice' : 'Acepto las condiciones y el aviso legal',
        'createAnAccount' : 'Crear cuenta',
        # Formulario de login
        'continueWithGoogle' : 'Continuar con google',
        # Selectores
        'islands' : 'Islas',
        'regions' : 'Comarcas',
        'SelectAnIsland' : 'Seleccione una isla',
        'SelectARegion' : 'Seleccione una comarca',
        'searchEngine' : 'Buscador',
        # Pagina principal
        'home.description' : '¿Qué es Puntua el mundo de las Islas Baleares? Es una comunidad apasionada por viajar y descubrir nuevas experiencias. Aquí, cada lugar cuenta una historia y guarda secretos esperando a ser revelados. Desde las playas de arena dorada hasta los acantilados escarpados, pasando por los pintorescos pueblos con encanto y las majestuosas montañas que pintan un paisaje inigualable. Nuestra misión es sencilla pero poderosa: brindarte la oportunidad de compartir tus aventuras y valorar tus experiencias. Queremos que seas el protagonista, y que tus opiniones sean una guía confiable para aquellos que también sueñan con conocer las maravillas de las Islas Baleares. Así que, ¿qué estás esperando? ¡Adéntrate en Puntua el mundo de las Islas Baleares y comienza a calificar, comentar y descubrir los lugares más increíbles de este paraíso mediterráneo! ¡Bienvenido a la experiencia Puntua el mundo de las Islas Baleares! ¡Bienvenido a las Islas Baleares!',
        'balearicIslands' : 'Islas Baleares',
        'explore' : 'Explorar',
        # Islas
        'isla.1' : 'Mallorca',
        'isla.2' : 'Menorca',
        'isla.3' : 'Formentera',
        'isla.4' : 'Ibiza'
    }
    return translations
"""