function createPublication()
{
    let placeNameText = document.getElementById('placeName').value;
    let selectedIslandId = document.getElementById('isla').value;
    let selectedRegionId = document.getElementById('comarca').value;
    let selectedTownId = document.getElementById('municipio').value;
    let selectedCategoryId = document.getElementById('categoria').value;
    let placeDescriptionText = document.getElementById('placeDescription').value;


    // Se crea el objeto que hará la petición a la API de Islas
    let comarcasRequest = new XMLHttpRequest();

    // Esta funcíon permite controlar el flujo de la petición y los estados
    // Los estados van del 0 al 4. A nosotros nos interesa únicamente el 4, que es el estado
    // de finalizaciòn de la petición
    // Cuando el estado ha llegado a 4 hay que comprobar el Status Code de la respuesta obtenida.
    // Para nosotros solo es valido el 200 en este caso.
    //  OJO: El contenido de la respuesta es DE TIPO STRING. Para poder gestionarlo hay que convertirlo a 
    // una colección de objetos o un objeto. Para nuestro caso particular tendremos una lista de comarcars.
    // La respuesta que devuelve es una cadena con formato JSON, por tanto, para parsearla como colección
    // de objetos, hay que usar el JSON.Parse
    // Una vez parseado la respuesta y guardada en una variable lo que hacemos es usarla para rellenar
    // el selector
    comarcasRequest.onreadystatechange = function()
    {
        if(this.readyState !== 4) return;

        if(this.status !== 201)
        {
            alert('Algo ha ido mal');
            return;
        }

        window.location.href = '/isla/'+selectedIslandId;
    }

    // OJO: Para hacer la petición, primero hay que abrir conexión (OPEN) y luego enviar (SEND)
    comarcasRequest.open('POST', '/publicacion/crear');
    comarcasRequest.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    
    let postData = {
        'placeName': placeNameText,
        'placeIsland': selectedIslandId,
        'placeRegion': selectedRegionId,
        'placeTown': selectedTownId,
        'placeCategory': selectedCategoryId,
        'placeDescription': placeDescriptionText
    };
    
    comarcasRequest.send(JSON.stringify(postData));
}