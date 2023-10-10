var comarcas = document.getElementById('comarca')
var municipios = document.getElementById('municipio')

// TODO: Eliminar, las islas ya viene pre-cargadas
// function cargarIslas() {
//     var array = ;
//     array.sort();
//     addOptions("isla", array);
//     comarcas.disabled = true;
//     municipios.disabled = true;
// }

function addOptions(domElement, array) {
    var selector = document.getElementsByName(domElement)[0];
    for(let i = 0; i < array.length; i++)
    {
        var opcion = document.createElement("option");
        opcion.text = array[i].name;
        opcion.value = array[i].id;
        selector.add(opcion);
    }
}

// Esta es la carga de comarcas via AJAX
function cargarComarcasDesdeAPI()
{
    let islas = document.getElementById('isla');
    let islaSeleccionada = islas.value;

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

        if(this.status !== 200)
        {
            alert('Algo ha ido mal');
            return;
        }

        comarcas.innerHTML = '<option value="">Seleccione una Comarca...</option>'
        comarcas.disabled = false;

        comarcasDeLaIsla = JSON.parse(this.responseText);
    
        comarcasDeLaIsla.forEach(function(comarca){
            let opcion = document.createElement('option')
            opcion.value = comarca.id;
            opcion.text = comarca.name;
            comarcas.add(opcion)
        });
    }

    // OJO: Para hacer la petición, primero hay que abrir conexión (OPEN) y luego enviar (SEND)
    comarcasRequest.open('GET', '/isla/' + islaSeleccionada + '/comarcas');
    comarcasRequest.send();
}


function cargarMunicipiosDesdeAPI()
{
    let comarcas = document.getElementById('comarca');
    let comarcaSeleccionada = comarcas.value;

    let municipiosRequest = new XMLHttpRequest();

    municipiosRequest.onreadystatechange = function()
    {
        if(this.readyState !== 4) return;

        if(this.status !== 200)
        {
            alert('Algo ha ido mal');
            return;
        }
        // municipios.innerHTML = '<option value="">Seleccione un Municipio...</option>'
        // municipios.disabled = false;
    
        municipiosDeComarca = JSON.parse(this.responseText);
    
        // municipiosDeComarca.forEach(function(municipio){
        //     let opcion = document.createElement('option');
        //     opcion.value = municipio.id;
        //     opcion.text = municipio.name;
        //     municipios.add(opcion);
        // });

        cargarTarjetas(municipiosDeComarca);
    }
    municipiosRequest.open('GET', '/comarca/' + comarcaSeleccionada + '/municipios');
    municipiosRequest.send();
}

function cargarTarjetas(towns) {
    
    containerCards = document.getElementById('container-cards');

    containerCards.innerHTML = ''; 
    
    towns.forEach(function(town) {
        let card = document.createElement('a');
        card.setAttribute('href', town.url);
        card.className = 'card';
        card.id = 'card';
        card.style.backgroundSize = '10%';
        card.innerHTML = '<div>' + '<h5>' + town.name + '</h5>' + '</div>';
        //card.innerHTML = '<h5>' + town.name + '</h5>';

        containerCards.appendChild(card);
    });
}


// function cargarMunicipios() {
//     var comarcaSeleccionada = comarca.value
    
//     municipios.innerHTML = '<option value="">Seleccione un Municipio...</option>'
//     municipios.disabled = false;

//     alert()

//     if(comarcaSeleccionada !== ''){
//         municipiosDeComarca = listaMunicipios[comarcaSeleccionada]
    
//         municipiosDeComarca.forEach(function(municipio){
//             let opcion = document.createElement('option')
//             opcion.value = municipio.id;
//             opcion.text = municipio.name;
//             municipios.add(opcion)
//         });
//     }
// }

function cargarMunicipiosAPI()
{
    let comarcas = document.getElementById('comarca');
    let comarcaSeleccionada = comarcas.value;

    let municipiosRequest = new XMLHttpRequest();

    municipiosRequest.onreadystatechange = function()
    {
        if(this.readyState !== 4) return;

        if(this.status !== 200)
        {
            alert('Algo ha ido mal');
            return;
        }
        municipios.innerHTML = '<option value="">Seleccione un Municipio...</option>'
        municipios.disabled = false;
    
        municipiosDeComarca = JSON.parse(this.responseText);
    
        municipiosDeComarca.forEach(function(municipio){
            let opcion = document.createElement('option');
            opcion.value = municipio.id;
            opcion.text = municipio.name;
            municipios.add(opcion);
        });

        cargarTarjetas(municipiosDeComarca);
    }
    municipiosRequest.open('GET', '/comarca/' + comarcaSeleccionada + '/municipios');
    municipiosRequest.send();
}
