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
            tableHeadings.forEach(head => head.classList.remove('active'));
            head.classList.add('active');
        }
    })
}

document.addEventListener('DOMContentLoaded', () => {
    let addPrescription = document.getElementById('addPrescription');
    if (addPrescription) {
        addPrescription.addEventListener('submit', (e) => {
            let orderDateValue = document.getElementById('order_date');
            let wasPickedUp = document.getElementById('picked_up');
            if (orderDateValue.value === '') {
                e.preventDefault();
                alert('Please Enter a Correct Order Date');
            }
            else if (wasPickedUp.value != 1 || wasPickedUp.value != 2) {
                e.preventDefault();
                alert('Please Select "Yes" or "No" for Was Picked Up');
            }
        });
    }
});

