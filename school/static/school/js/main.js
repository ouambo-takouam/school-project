//*** SIDE NAVIGATION ***/

/**--- Ajout et suppression de la classe 'active' sur les elements de navigation ---**/
const listItems = document.querySelectorAll(
  ".sidebar .sidebar-menu > ul > li.submenu-open ul > li:not(.submenu)"
);

// Fonction pour gérer le clic sur un élément <li>
function toggleActiveClass() {
  // Retirer la classe 'active' de tous les éléments <li>
  listItems.forEach((item) => {
    item.classList.remove("active");
  });

  // Ajouter la classe 'active' uniquement à l'élément cliqué
  this.classList.toggle("active");
}

// Ajout d'un écouteur d'événement au clic pour chaque élément <li>
listItems.forEach((item) => {
  item.addEventListener("click", toggleActiveClass);
});



/**--- Gestion apparition et disparition des sous-menus  ---**/
var dropdownList = document.getElementsByClassName("dropdown-btn");

for (let i = 0; i < dropdownList.length; i++) {
  dropdownList[i].addEventListener("click", function () {
    var ul = this.nextElementSibling;
    
    if (ul.style.display === "block") {
      ul.style.display = "none";
    } else {
      ul.style.display = "block";
    }
  });
}

// Gestion deroulement du nav-profile
var navprofilelink = document.getElementById("nav-profile-link");

navprofilelink.addEventListener("click", function () {
  var navprofile = this.nextElementSibling;

  if (navprofile.style.display === "grid") {
    navprofile.style.display = "none";
  } else {
    navprofile.style.display = "grid";
  }
});
