document.addEventListener('DOMContentLoaded', function () {
  var searchInput = document.getElementById('project-search');
  var searchButton = document.getElementById('search-button');

  if (searchInput && searchButton) {
      searchInput.addEventListener('input', function () {
          var searchTerm = this.value.toLowerCase();
          var projects = document.querySelectorAll('#projects-row .eshkere');

          projects.forEach(function (project) {
              var title = project.querySelector('.project-title-author p').textContent.toLowerCase();
              var author = project.querySelector('.project-title-author a').textContent.toLowerCase();

              if (title.includes(searchTerm) || author.includes(searchTerm)) {
                  project.style.display = '';
              } else {
                  project.style.display = 'none';
              }
          });
      });

      searchButton.addEventListener('click', function () {
          var searchTerm = searchInput.value.toLowerCase();
          var projects = document.querySelectorAll('#projects-row .eshkere');

          projects.forEach(function (project) {
              var title = project.querySelector('.project-title-author p').textContent.toLowerCase();
              var author = project.querySelector('.project-title-author a').textContent.toLowerCase();

              if (title.includes(searchTerm) || author.includes(searchTerm)) {
                  project.style.display = '';
              } else {
                  project.style.display = 'none';
              }
          });
      });
  }
});