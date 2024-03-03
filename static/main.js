let horizontalUnderLine = document.getElementById("horizontal-underline");
let navbarSiteLinks = document.querySelectorAll(".navbar-site-links:first-child a");

navbarSiteLinks.forEach(link => link.addEventListener("mouseover", (e) => horizontalIndicator(e)))

function horizontalIndicator(e) {
    horizontalUnderLine.style.left = e.currentTarget.offsetLeft + "px";
    horizontalUnderLine.style.width = e.currentTarget.offsetWidth + "px";
    horizontalUnderLine.style.top = e.currentTarget.offsetTop + e.currentTarget.offsetHeight + "px";
}

