const userStars = document.querySelectorAll(".user-stars .star");
const submitButton = document.getElementById("submit-rating");
const userComment = document.getElementById("user-comment");
const userRatingsContainer = document.querySelector(".user-ratings");
const publicationId = document.getElementById("publicationId");
const placeValorationText = document.getElementById("starsNumbers")

userStars.forEach((star, index) => {
    star.addEventListener("click", () => {
        userStars.forEach((s, i) => {
            if (i <= index) {
                s.classList.add("active");
            } else {
                s.classList.remove("active");
            }
        });
    });
});


submitButton.addEventListener("click", () => {
    const selectedStars = document.querySelectorAll(".user-stars .star.active").length;
    const comment = userComment.value.trim();
    if (selectedStars > 0 && comment !== "") {
        createValoratrion("Usuario Anónimo", selectedStars, comment);
        clearRatingForm();
    }
});


// function addRating(username, stars, comment) {

//     const newRating = document.createElement("div");
//     newRating.className = "user-rating";
//     newRating.innerHTML = `
//         <h3>${username}</h3>
//         <div class="user-stars">
//             ${"★".repeat(stars)}
//             ${"☆".repeat(5 - stars)}
//         </div>
//         <p>${comment}</p>
//     `;
//     userRatingsContainer.appendChild(newRating);
// }

function clearRatingForm() {
    userStars.forEach(star => star.classList.remove("active"));
    userComment.value = "";
}


function createValoratrion(username, stars, comment){
    let placeDescriptionText = document.getElementById('user-comment').value;

    let valorationsRequest = new XMLHttpRequest();

    const newRating = document.createElement("div");
    newRating.className = "user-rating";
    newRating.innerHTML = `
        <h3>${username}</h3>
        <div class="user-stars">
            ${"★".repeat(stars)}
            ${"☆".repeat(5 - stars)}
        </div>
        <p>${comment}</p>
    `;
    placeValorationText.value = stars;
    //let placeValorationText = userRatingsContainer.appendChild(newRating);

    valorationsRequest.onreadystatechange = function()
    {
        if(this.readyState !== 4) return;

        if(this.status !== 201)
        {
            alert('Algo ha ido mal');
            return;
        }

        window.location.href = '/valoration/' + publicationId.value;
    }
    valorationsRequest.open('POST', '/valoration/crear');
    valorationsRequest.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    let postValorationData = {
        'placeDescription': placeDescriptionText,
        'placeValoration': placeValorationText.value,
        'placePublicationId': publicationId.value
    };
    console.log(postValorationData)

    valorationsRequest.send(JSON.stringify(postValorationData));
}