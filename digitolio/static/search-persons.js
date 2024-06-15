document.addEventListener('DOMContentLoaded', function() {
    var searchInput = document.getElementById('search-persons');
    var searchButton = document.getElementById('search-button');

    function filterUsers() {
        var searchTerm = searchInput.value.toLowerCase();
        var userRows = document.querySelectorAll('.user-card');

        userRows.forEach(function(userCard) {
            var userName = userCard.querySelector('.main-info a p:first-child').textContent.toLowerCase();
            var userSurname = userCard.querySelector('.main-info a p:nth-child(2)').textContent.toLowerCase();
            var userUsername = userCard.querySelector('.main-info a p:nth-child(3)').textContent.toLowerCase();

            var match = userName.includes(searchTerm) || userSurname.includes(searchTerm) || userUsername.includes(searchTerm);
            userCard.parentNode.style.display = match ? 'block' : 'none';

            var projectCards = userCard.parentNode.parentNode.querySelectorAll('.col:not(:first-child)');
            projectCards.forEach(function(projectCard) {
                projectCard.style.display = match ? 'block' : 'none';
            });
        });
    }

    searchInput.addEventListener('input', filterUsers);
    searchButton.addEventListener('click', filterUsers);
});