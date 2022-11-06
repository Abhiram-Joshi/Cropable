from django.shortcuts import render

from decouple import config
from django.contrib.auth.decorators import login_required

import requests

# Create your views here.
@login_required
def weatherView(request):
    url = "http://api.weatherapi.com/v1/forecast.json"

    query_params = {
        "key": config("API_KEY"),
        "q": "Kolkata",
        "days": 10,
        "aqi": "no",
    }

    response = requests.get(url, params=query_params)
    data = response.json()

    forecast = list()

    for forecast_data in data["forecast"]["forecastday"]:
        forecast.append({
            "date": forecast_data["date"],
            "forecast": {
                "maxtemp_c": forecast_data.get("day").get("maxtemp_c"),
                "mintemp_c": forecast_data.get("day").get("mintemp_c"),
                "maxwind_mph": forecast_data.get("day").get("maxwind_mph"),
                "maxwind_kph": forecast_data.get("day").get("maxwind_kph"),
                "totalprecip_mm": forecast_data.get("day").get("totalprecip_mm"),
                "totalprecip_in": forecast_data.get("day").get("totalprecip_in"),
                "totalsnow_cm": forecast_data.get("day").get("totalsnow_cm"),
                "sunrise": forecast_data.get("astro").get("sunrise"),
                "sunset": forecast_data.get("astro").get("sunset"),
            }
        })

    return render(request, "weather.html", context={"forecast": forecast})