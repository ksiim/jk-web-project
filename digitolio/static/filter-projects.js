let newButton = document.getElementById('new');
let oldButton = document.getElementById('old');
let rateButton = document.getElementById('rate');

let projectsContainer = document.getElementById('projects-row')//.querySelectorAll('.col');

function parseCustomDate(dateString) {
    const months = {
        'января': '01',
        'февраля': '02',
        'марта': '03',
        'апреля': '04',
        'мая': '05',
        'июня': '06',
        'июля': '07',
        'августа': '08',
        'сентября': '09',
        'октября': '10',
        'ноября': '11',
        'декабря': '12'
    };
    const parts = dateString.split(' ');
    const day = parts[0];
    const month = months[parts[1]];
    const year = parts[2];
    const hours = parts[4].split(':')[0];
    const minutes = parts[4].split(':')[1];
    return new Date(`${year}-${month}-${day}T${hours}:${minutes}:00`);
}

newButton.addEventListener('change', function() {
    let projectsArray = Array.from(projectsContainer.querySelectorAll('.col'));
    projectsArray.sort(function(a, b) {
        let dateA = parseCustomDate(a.getAttribute('data-time_created'));
        let dateB = parseCustomDate(b.getAttribute('data-time_created'));
        return dateB - dateA;
    });
    while (projectsContainer.firstChild) {
        projectsContainer.removeChild(projectsContainer.firstChild);
    }
    
    // Добавляем отсортированные элементы обратно в контейнер
    projectsArray.forEach(function(item) {
        projectsContainer.appendChild(item);
    });
});

oldButton.addEventListener('change', function() {
    let projectsArray = Array.from(projectsContainer.querySelectorAll('.col'));
    projectsArray.sort(function(a, b) {
        let dateA = parseCustomDate(a.getAttribute('data-time_created'));
        let dateB = parseCustomDate(b.getAttribute('data-time_created'));
        return dateA - dateB;
    });
    while (projectsContainer.firstChild) {
        projectsContainer.removeChild(projectsContainer.firstChild);
    }
    
    // Добавляем отсортированные элементы обратно в контейнер
    projectsArray.forEach(function(item) {
        projectsContainer.appendChild(item);
    });
});

rateButton.addEventListener('change', function() {
    let projectsArray = Array.from(projectsContainer.querySelectorAll('.col'));
    projectsArray.sort(function(a, b) {
        let intA = parseInt(a.getAttribute('data-grade'));
        
        let intB = parseInt(b.getAttribute('data-grade'));
        if (intA < intB) {
            return 1;
        }
        if (intA > intB) {
            return -1;
        }
        return 0;
    });
    while (projectsContainer.firstChild) {
        projectsContainer.removeChild(projectsContainer.firstChild);
    }
    
    // Добавляем отсортированные элементы обратно в контейнер
    projectsArray.forEach(function(item) {
        projectsContainer.appendChild(item);
    });
});

let languageFilter = document.getElementById('filter2');
let tagFilter = document.getElementById('filter1');

languageFilter.addEventListener('change', function() {
    let projectsArray = Array.from(projectsContainer.querySelectorAll('.col'));
    console.log(projectsArray);
    let language = languageFilter.value;
    projectsArray.forEach(function(item) {
        if (language === 'Выберите язык') {
            item.classList.remove('hidden');
        } else {
            let itemLanguage = item.getAttribute('data-language');
            if (itemLanguage !== language) {
                item.classList.add('hidden');
            } else {
                item.classList.remove('hidden');
            }
        }
    });
});

tagFilter.addEventListener('change', function() {
    let projectsArray = Array.from(projectsContainer.querySelectorAll('.col'));
    let tag = tagFilter.value;
    projectsArray.forEach(function(item) {
        if (tag === 'Выберите тег') {
            item.style.display = 'block';
        } else {
            let itemTags = item.getAttribute('data-tags').split(', ');
            if (!itemTags.includes(tag)) {
                item.style.display = 'none';
            } else {
                item.style.display = 'block';
            }
        }
    });
});