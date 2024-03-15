// Responsive underline bar for nav links
let horizontalUnderLine = document.getElementById("horizontal-underline");
let navbarSiteLinks = document.querySelectorAll(".navbar-site-links li a");
let currentActiveLink;
// hover effect when mouse over nav links
navbarSiteLinks.forEach(link => {
    link.addEventListener("mouseover", (e) => {
        horizontalIndicator(e.currentTarget);
        currentActiveLink = e.currentTarget;
    })
})
// position the underline bar for nav links
function horizontalIndicator(linkElement) {
    horizontalUnderLine.style.left = linkElement.offsetLeft + "px";
    horizontalUnderLine.style.width = linkElement.offsetWidth + "px";
    horizontalUnderLine.style.top = linkElement.offsetTop + linkElement.offsetHeight + "px";
}
// when browser gets resized, move its position according to the size
window.addEventListener('resize', () => {
    if (currentActiveLink) {
        horizontalIndicator(currentActiveLink);
    }
});

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

// Check for any null values 
document.addEventListener('DOMContentLoaded', () => {
    function checkFormFields(formId, fields) {
        let form = document.getElementById(formId);
        // if form exists
        if (form) {
            form.addEventListener('submit', (e) => {
                // loop through the form and its fields
                for (let fieldId of fields) {
                    let field = document.getElementById(fieldId);
                    if (form === 'modPrescription') {
                        if (!field || field.value === '') {
                            e.preventDefault();
                            alert(`Please Enter a Corerct ${fieldId.replace('_', ' ')}`);
                        }
                    }
                    // check for their values for conditionals
                    else if (!field || field.value === '' || field.value <= 0) {
                        e.preventDefault();
                        alert(`Please Enter a Correct ${fieldId.replace('_', ' ')}`);
                        break;
                    }
                }
            });
        }
    }

    // 'Adding/Editing Medications' 
    checkFormFields('modMeds', ['Name', 'Cost']);
    // 'Adding/Editing Owners' 
    checkFormFields('modOwner', ['Name', 'Address', 'Phone Number']);
    // 'Adding/Editing Prescriptions'
    checkFormFields('modPrescription', ['Order Date', 'Was Picked Up']);
    // 'Adding/Editing Pets'
    checkFormFields('modPet', ['Name', 'Breed', 'Age', 'Gender']);
    // 'Adding/Editing Vets'
    checkFormFields('modVet', ['Name', 'Clinic', 'Email']);
    // 'Adding prescriptionMedications'
    checkFormFields('addpm', ['Quantity']);
});