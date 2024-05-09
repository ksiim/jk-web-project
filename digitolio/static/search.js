
document.addEventListener('DOMContentLoaded', function() {
    var searchInput = document.querySelector('#project-search');
  
    function performSearch() {
      var searchQuery = searchInput.value;
  
      fetch('search/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ query: searchQuery })
      })
        .then(response => response.json())
        .then(data => {
            console.log(data); 
            var projectsContainer = document.getElementById('projects-row');
            projectsContainer.innerHTML = '';
            data.projects.forEach(project => {
                var projectElement = document.createElement('a');
                projectElement.classList.add('text-decoration-none');
                projectElement.style.color = 'black';
                projectElement.href = '/project/' + project.id;

                var colElement = document.createElement('div');
                colElement.classList.add('col', 'mb-4');
                colElement.style.height = '10vw';
                projectElement.appendChild(colElement);

                var divElement = document.createElement('div');
                divElement.classList.add('h-100');
                divElement.style.backgroundColor = '#BBE4F5';
                divElement.style.borderRadius = '1rem';
                colElement.appendChild(divElement);

                var cardBodyElement = document.createElement('div');
                cardBodyElement.classList.add('card-body');
                divElement.appendChild(cardBodyElement);

                var titleElement = document.createElement('h5');
                titleElement.classList.add('card-title');
                titleElement.textContent = project.title;
                cardBodyElement.appendChild(titleElement);

                var descriptionElement = document.createElement('p');
                descriptionElement.classList.add('card-text');
                descriptionElement.textContent = project.description.substring(0, 110);
                cardBodyElement.appendChild(descriptionElement);

                projectsContainer.appendChild(projectElement);
            });
        });
    }
  
    searchInput.addEventListener('keypress', function(event) {
      if (event.key === 'Enter') {
        performSearch();
      }
    });
  });
  
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  
