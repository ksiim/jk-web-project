let newButton = document.getElementById('new');
let oldButton = document.getElementById('old');
let rateButton = document.getElementById('rate');

let projectsContainer = document.getElementById('projects-row');

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

function applyChanges() {
    let projectsArray = Array.from(projectsContainer.querySelectorAll('.col'));
    let languageFilter = document.getElementById('filter2');
    let tagFilter = document.getElementById('filter1');
    let language = languageFilter.value;
    let tag = tagFilter.value;

    projectsArray.forEach(function(item) {
        let itemLanguage = item.getAttribute('data-language');
        let itemTags = item.getAttribute('data-tags').split(', ');

        let dateA = parseCustomDate(item.getAttribute('data-time_created'));
        let intA = parseInt(item.getAttribute('data-grade'));

        if (language === 'Выберите язык' && tag === 'Выберите тег') {
            item.classList.remove('hidden');
            item.style.display = 'block';
        } else if (language === 'Выберите язык') {
            if (!itemTags.includes(tag)) {
                item.classList.add('hidden');
                item.style.display = 'none';
            } else {
                item.classList.remove('hidden');
                item.style.display = 'block';
            }
        } else if (tag === 'Выберите тег') {
            if (itemLanguage !== language) {
                item.classList.add('hidden');
                item.style.display = 'none';
            } else {
                item.classList.remove('hidden');
                item.style.display = 'block';
            }
        } else {
            if (itemLanguage !== language || !itemTags.includes(tag)) {
                item.classList.add('hidden');
                item.style.display = 'none';
            } else {
                item.classList.remove('hidden');
                item.style.display = 'block';
            }
        }
    });

    if (newButton.checked) {
        projectsArray.sort(function(a, b) {
            let dateA = parseCustomDate(a.getAttribute('data-time_created'));
            let dateB = parseCustomDate(b.getAttribute('data-time_created'));
            return dateB - dateA;
        });
    } else if (oldButton.checked) {
        projectsArray.sort(function(a, b) {
            let dateA = parseCustomDate(a.getAttribute('data-time_created'));
            let dateB = parseCustomDate(b.getAttribute('data-time_created'));
            return dateA - dateB;
        });
    } else if (rateButton.checked) {
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
    }

    while (projectsContainer.firstChild) {
        projectsContainer.removeChild(projectsContainer.firstChild);
    }

    projectsArray.forEach(function(item) {
        projectsContainer.appendChild(item);
    });
}

let applyButton = document.getElementById('apply-changes');

applyButton.addEventListener('click', applyChanges);
