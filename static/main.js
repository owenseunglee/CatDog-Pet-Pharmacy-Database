let horizontalUnderLine = document.getElementById("horizontal-underline");
let navbarSiteLinks = document.querySelectorAll(".navbar-site-links:first-child a");

navbarSiteLinks.forEach(link => link.addEventListener("mouseover", (e) => horizontalIndicator(e)))

function horizontalIndicator(e) {
    horizontalUnderLine.style.left = e.currentTarget.offsetLeft + "px";
    horizontalUnderLine.style.width = e.currentTarget.offsetWidth + "px";
    horizontalUnderLine.style.top = e.currentTarget.offsetTop + e.currentTarget.offsetHeight + "px";
}

const confirmRedirect = () => {
    if (confirm('Are you sure you want to go back?')) {
        window.location.href = "owners";
    }
}

window.onload = function () {
    let tableHeadings = document.querySelectorAll("thead th");

    tableHeadings.forEach((head) => {
        head.onclick = () => {
            console.log("its working");
            tableHeadings.forEach(head => head.classList.remove('active'));
            head.classList.add('active');
        }
    })
}