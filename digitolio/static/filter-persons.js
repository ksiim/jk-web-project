let groupSortForm = document.getElementById('group');
let yearSortForm = document.getElementById('year');
let groupForm = document.getElementById('filter2');
let languageForm = document.getElementById('filter3');

let usersContainer = document.querySelector('.container .p-4');

function applyChanges() {
    let usersArray = Array.from(usersContainer.querySelectorAll('.row row-cols-auto'));
    console.log(usersArray);
    let group = groupForm.value;
    let language = languageForm.value;

    usersArray.forEach(function(item) {
        let itemGroup = item.getAttribute('data-group');
        let itemLanguage = item.getAttribute('data-language');
        if (language === 'Выберите язык' && group === 'Выберите группу') {
            item.classList.remove('hidden');
            item.style.display = 'flex';
        } else if (language === 'Выберите язык') {
            if (itemGroup !== group) {
                item.classList.add('hidden');
                item.style.display = 'none';
            } else {
                item.classList.remove('hidden');
                item.style.display = 'flex';
            }
        } else if (group === 'Выберите группу') {
            if (itemLanguage !== language) {
                item.classList.add('hidden');
                item.style.display = 'none';
            } else {
                item.classList.remove('hidden');
                item.style.display = 'flex';
            }
        } else {
            if (itemGroup !== group || itemLanguage !== language) {
                item.classList.add('hidden');
                item.style.display = 'none';
            } else {
                item.classList.remove('hidden');
                item.style.display = 'flex';
            }
        }

        if (yearSortForm.checked) {
            usersArray.sort(function(a, b) {
                let intA = a.getAttribute('data-year');
                let intB = b.getAttribute('data-year');
                if (intA > intB) {
                    return 1;
                }
                if (intA < intB) {
                    return -1;
                }
                return 0;
            });
        }
        if (groupSortForm.checked) {
            usersArray.sort(function(a, b) {
                let A = a.getAttribute('data-group');
                let B = b.getAttribute('data-group');
                if (A < B) {
                    return 1;
                }
                if (A > B) {
                    return -1;
                }
                return 0;
            });
        }
        while (usersContainer.firstChild) {
            usersContainer.removeChild(usersContainer.firstChild);
        }
    
        usersArray.forEach(function(item) {
            usersContainer.appendChild(item);
        });
        if (usersArray.length === usersContainer.querySelectorAll('.hidden').length) {
            let noResults = document.createElement('div');
            noResults.classList.add('text-center', 'w-100');
            noResults.textContent = 'Нет результатов';
            usersContainer.appendChild(noResults);
        }
    });
}

let applyButton = document.getElementById('apply-changes');

applyButton.addEventListener('click', applyChanges);
