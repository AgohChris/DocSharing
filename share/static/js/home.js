document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const documentCards = document.querySelectorAll('.document-card');

    searchInput.addEventListener('input', function() {
        const searchTerm = searchInput.value.toLowerCase();
        documentCards.forEach(card => {
            const title = card.querySelector('h3').textContent.toLowerCase();
            const username = card.querySelector('p').textContent.toLowerCase();
            if (title.includes(searchTerm) || username.includes(searchTerm)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    });
});



const mobileNav = document.querySelector(".hamburger");
const navbar = document.querySelector(".menubar");

const toggleNav = () => {
  navbar.classList.toggle("active");
  mobileNav.classList.toggle("hamburger-active");
};
mobileNav.addEventListener("click", () => toggleNav());
