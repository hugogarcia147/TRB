const selector = document.getElementById('opciones');

selector.addEventListener('change', function() {
    const opcionSeleccionada = selector.value;
    //Aquí hay que guardar la cookie

    document.cookie = 'language=' + opcionSeleccionada;

    //alert(document.cookie);

    location.reload();

});