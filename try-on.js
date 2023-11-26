
document.addEventListener('DOMContentLoaded', function () {
    var lookupButton = document.getElementById('lookup');
    var lookupCitiesButton = document.getElementById('lookupCities');
    var countryInput = document.getElementById('country');

    lookupButton.addEventListener('click', function () {
        lookupData('country');
    });

    lookupCitiesButton.addEventListener('click', function () {
        lookupData('cities');
    });

    function lookupData(lookupType) {
        var country = countryInput.value;
        var xhr = new XMLHttpRequest();
        xhr.open('GET', 'world.php?country=' + encodeURIComponent(country) + '&lookup=' + encodeURIComponent(lookupType), true);

        xhr.onload = function () {
            if (xhr.status >= 200 && xhr.status < 400) {
                document.getElementById('result').innerHTML = xhr.responseText;
            } else {
                console.error('Error: ' + xhr.status);
            }
        };

        xhr.onerror = function () {
            console.error('Request failed');
        };

        xhr.send();
    }
});