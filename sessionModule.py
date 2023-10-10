from flask import request

def get_language():
    language = request.cookies.get('language')
    if language is None:
        language = 1
    return int(language)