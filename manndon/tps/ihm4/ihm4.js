const texte = document.querySelector("i");
let index = 0;
const couleur = ["darkkhaki", "red", "aqua", "chartreuse", "gold"];
texte.style.color = couleur[index];
function changeCouleur() {
    index = (index + 1) % couleur.length;
    texte.style.color = couleur[index];
}

texte.addEventListener("mouseover", changeCouleur);

const secret = document.getElementById("secret");
let nombreClick = 0;
function montreTexte() {
    nombreClick++;
    if (nombreClick % 2 == 1) {
        secret.innerHTML = "Bonjour :)";
        secret.style.height = "50px";
    }
    else {
        secret.innerHTML = "";
        secret.style.height = "20px";
    }
}

secret.addEventListener("click", montreTexte);