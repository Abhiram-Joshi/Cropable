from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# from django.contrib.gis.utils import GeoIP

from .forms import ReminderForm
from .models import ReminderModel

from decouple import config
import requests
from django_q.tasks import schedule
from django_q.models import Schedule
import datetime
from datetime import timedelta
import geocoder
import pytz

# Create your views here.
@login_required
def weatherView(request):
    url = "http://api.weatherapi.com/v1/forecast.json"

    query_params = {
        "key": config("API_KEY"),
        "q": "Vellore",
        "days": 10,
        "aqi": "no",
    }

    response = requests.get(url, params=query_params)
    print(response)
    data = response.json()

    forecast = list()

    # print(data)
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

@login_required
def soilView(request):
    ip = request.META.get("REMOTE_ADDR")
    if ip and ip != "127.0.0.1":
        g = geocoder.ip(ip)
    else:
        g = geocoder.ip('me')
        # print("#")

    # print(g.latlng)
    # url = f"https://api.ambeedata.com/soil/latest/by-lat-lng?lat={g.latlng[0]}&lng={g.latlng[1]}"
    # url = f"https://api.ambeedata.com/soil/latest/by-lat-lng?lat=13&lng=80"
    # headers = {
    #     "x-api-key": config("SOIL_API_KEY"),
    #     'Content-type': "application/json"
    # }

    # response = requests.get(url, headers=headers)
    # print(response)
    # response_json = response.json()
    # print(response_json)

    # return render(request, "soil.html", context={"soil_data": response_json.get("data")[0]})

    url = f"http://api.agromonitoring.com/agro/1.0/soil"
    params = {
        "appid": config("AGROMONITORING_APP_ID"),
        "polyid": "6434f3f1ff8d76000713327a",
    }

    response = requests.get(url, params=params)
    response_json = response.json()
    print(response_json)

    return render(request, "soil.html", context={"soil_data": response_json})

@login_required
def setReminderView(request):
    if request.method == "POST":
        form = ReminderForm(request.POST)

        if form.is_valid():
            # LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
            # print((form.cleaned_data.get("datetime").replace(tzinfo=LOCAL_TIMEZONE) - datetime.datetime.now().replace(tzinfo=LOCAL_TIMEZONE)).total_seconds()//60)
            # print(form.cleaned_data.get("datetime").tzinfo)

            # schedule(
            #     # ReminderModel.objects.create,
            #     # kwargs = {
            #     #     "user": request.user,
            #     #     "title": form.cleaned_data.get("title"),
            #     #     "description": form.cleaned_data.get("description"),
            #     #     "date": form.cleaned_data.get("datetime"),
            #     # },
            #     "print",
            #     2,
            #     schedule_type=Schedule.ONCE,
            #     # next_run = form.cleaned_data.get("datetime").astimezone(pytz.utc),
            #     next_run = timezone.now() + timedelta(minutes=1),
            #     # minutes = int((form.cleaned_data.get("datetime").replace(tzinfo=LOCAL_TIMEZONE) - datetime.datetime.now().replace(tzinfo=LOCAL_TIMEZONE)).total_seconds()//60),
            # )

            # return redirect(reverse("home"))
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            return redirect(reverse("home"))
        
        else:
            print(form.errors)
            print(form.non_field_errors)
            form = ReminderForm()
    
    else:
        form = ReminderForm()

    return render(request, "reminder.html", context = {"form": form, "labels": ["Title", "Description", "Date and Time"]})

@login_required
def getReminderView(request):
    reminders = ReminderModel.objects.filter(user=request.user).filter(datetime__gte=datetime.datetime.now()).order_by("-datetime")
    return render(request, "reminders_view.html", context={"reminders": reminders})