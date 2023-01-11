let page = 0;
function toggleDisplay(event) {
  if (event.key == "ArrowUp") {
    if (page != 0) {
      page += 100;
    }
    document.querySelector("body").style.transform = "translateY(" + page.toString() + "vh)";
  }
  else if (event.key == "ArrowDown") {
    if (page != -200) {
      page -= 100;
    }
    document.querySelector("body").style.transform = "translateY(" + page.toString() + "vh)";
  }
}

function retourne() {
  page = -200;
  document.querySelector("section:nth-child(2)").scrollIntoView();
}

window.addEventListener('keydown', toggleDisplay);
document.querySelector(".zone_interdite").addEventListener("mouseover", retourne)