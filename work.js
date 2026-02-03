// ====== MENU TOGGLE FOR MOBILE ======
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('nav ul');

menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

// ====== SMOOTH SCROLLING ======
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });

        // Close menu on mobile after clicking
        navLinks.classList.remove('active');
    });
});

// ====== OPEN PROJECT IN NEW TAB ======
function openProject(url) {
    window.open(url, '_blank');
}

// ====== OPEN CERTIFICATE IMAGE IN NEW TAB ======
function openImage(url) {
    window.open(url, '_blank');
}