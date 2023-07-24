var comarcas = document.getElementById('comarca')
var municipios = document.getElementById('municipio')

function cargarIslas() {
    var array = ["Mallorca", "Menorca", "Ibiza", "Formentera"];
    array.sort();
    addOptions("isla", array);
    comarcas.disabled = true;
}

function addOptions(domElement, array) {
    var selector = document.getElementsByName(domElement)[0];
    for (isla in array) {
        var opcion = document.createElement("option");
        opcion.text = array[isla];
        opcion.value = array[isla].toLowerCase()
        selector.add(opcion);
    }
}


function cargarComarcas() {
    var listaComarcas = {
        mallorca: ["1.1", "2.1", "3.1", "4.1", "5.1"],
        menorca: ["1.2", "2.2", "3.2", "4.2", "5.2"],
        ibiza: ["1.3", "2.3", "3.3", "4.3", "5.3"],
        formentera: ["1.4", "2.4", "3.4", "4.4", "5.4"]
    }
    
    var islas = document.getElementById('isla')
    var comarcas = document.getElementById('comarca')
    var islaSeleccionada = islas.value
    
    comarcas.innerHTML = '<option value="">Seleccione una Comarca...</option>'
    comarcas.disabled = false;

    if(islaSeleccionada !== ''){
        islaSeleccionada = listaComarcas[islaSeleccionada]
        islaSeleccionada.sort()
    
        islaSeleccionada.forEach(function(comarca){
        let opcion = document.createElement('option')
        opcion.value = comarca
        opcion.text = comarca
        comarcas.add(opcion)
        });
    }
}

cargarIslas();

/*
function cargarMunicipios() {
    var listaMunicipios = {
        1.1: ["Hola", "Hola", "Hola"],
        1.2: ["Adios", "Adios", "Adios"],
        1.3: ["Que tal", "Que tal", "Que tal"],
        1.4: ["Soy yo", "Soy yo", "Soy yo"]
    }
    
    var comarca = document.getElementById('comarca')
    var municipios = document.getElementById('municipio')
    var comarcaSeleccionada = comarca.value
    
    municipios.innerHTML = '<option value="">Seleccione un Municipio...</option>'
    municipios.disabled = false;

    if(islaSeleccionada !== ''){
        comarcaSeleccionada = listaMunicipios[comarcaSeleccionada]
        comarcaSeleccionada.sort()
    
        comarcaSeleccionada.forEach(function(municipio){
        let opcion = document.createElement('option')
        opcion.value = municipio
        opcion.text = municipio
        municipios.add(opcion)
        });
    }
}
*/
