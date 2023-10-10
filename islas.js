let islanId = document.getElementById('islId').value;

function cargarTarjetas(publications) {
    
    containerCards = document.getElementById('container-cards');

    containerCards.innerHTML = ''; 
    
    publications.forEach(function(publication) {
        let div = document.createElement('div');
        let card = document.createElement('a');
        card.setAttribute('href', publication.url);
        div.className = 'card';
        div.style.backgroundImage = "url(/static/img/categorias/" + publication.image + ".jpg)";
        div.innerHTML = '<h5>' + publication.title + '</h5>' + '<p class="valoration">' + publication.valoration + '</p>' + '<p class="data">' + publication.dataCreate + '</p>'
        card.appendChild(div);
        
        // card.innerHTML = '<div>' + '<h5>' + publication.title + '</h5>' + '<p class="valoration">' + publication.valoration + '</p>' + '<p class="data">' + publication.dataCreate + '</p>' + '</div>';
        // card.innerHTML = '<p>' + publication.description + '</p>';
        containerCards.appendChild(card);
    });
}


function cargarPublicacionesDesdeAPI()
{
    let category = document.getElementById('categories');
    let selectedCategory = category.value;

    let publicationsRequest = new XMLHttpRequest();

    publicationsRequest.onreadystatechange = function()
    {
        if(this.readyState !== 4) return;

        if(this.status !== 200)
        {
            alert('Algo ha ido mal');
            return;
        }
    
        publications = JSON.parse(this.responseText);
    

        cargarTarjetas(publications);
        //alert(publications)
    }
    publicationsRequest.open('GET', '/publicacion/' + islanId + '/' + selectedCategory );
    publicationsRequest.send();
}