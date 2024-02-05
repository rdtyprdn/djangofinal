var kandidat1 = document.getElementById('kandidat1');
var myRadio1 = document.getElementById('myRadio1');

kandidat1.addEventListener('click', function() {
    toggleCheckboxState(kandidat1, myRadio1);
});

var kandidat2 = document.getElementById('kandidat2');
var myRadio2 = document.getElementById('myRadio2');

kandidat2.addEventListener('click', function() {
    toggleCheckboxState(kandidat2, myRadio2);
});

function toggleCheckboxState(kandidat, radio) {
    if (!radio.checked) {
        kandidat.classList.add('checked');
        radio.checked = true;

        if (radio === myRadio1) {
            kandidat2.classList.remove('checked');
            myRadio2.checked = false;
        }else {
            kandidat1.classList.remove('checked');
            myRadio1.checked = false;
        }
    } 
};

