function getWeather() {
    var city = document.getElementById("cityInput").value;
    var apiKey = "AIzaSyCxM-0UkLWGnsIDjWmQncE1hlZv5pHlaHE"; // Replace with your API key

    // Make a request to the weather API
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "https://api.weatherapi.com/v1/current.json?key=" + apiKey + "&q=" + city, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            displayWeather(response);
        }
    };
    xhr.send();
}

function displayWeather(weatherData) {
    var weatherInfo = document.getElementById("weatherInfo");
    weatherInfo.innerHTML = "";

    var location = weatherData.location.name + ", " + weatherData.location.region + ", " + weatherData.location.country;
    var temperature = weatherData.current.temp_c + "°C";
    var condition = weatherData.current.condition.text;

    var locationElement = document.createElement("p");
    locationElement.textContent = "Location: " + location;
    weatherInfo.appendChild(locationElement);

    var temperatureElement = document.createElement("p");
    temperatureElement.textContent = "Temperature: " + temperature;
    weatherInfo.appendChild(temperatureElement);

    var conditionElement = document.createElement("p");
    conditionElement.textContent = "Condition: " + condition;
    weatherInfo.appendChild(conditionElement);
}