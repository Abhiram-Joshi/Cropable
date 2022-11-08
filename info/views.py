from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .forms import ReminderForm
from .models import ReminderModel

from decouple import config
import requests
from django_q.tasks import schedule
from django_q.models import Schedule
import datetime
from datetime import timedelta
import pytz

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

@login_required
def setReminderView(request):
    if request.method == "POST":
        form = ReminderForm(request.POST)

        if form.is_valid():
            LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
            # print((form.cleaned_data.get("datetime").replace(tzinfo=LOCAL_TIMEZONE) - datetime.datetime.now().replace(tzinfo=LOCAL_TIMEZONE)).total_seconds()//60)
            print(form.cleaned_data.get("datetime").tzinfo)

            schedule(
                # ReminderModel.objects.create,
                # kwargs = {
                #     "user": request.user,
                #     "title": form.cleaned_data.get("title"),
                #     "description": form.cleaned_data.get("description"),
                #     "date": form.cleaned_data.get("datetime"),
                # },
                "print",
                2,
                schedule_type=Schedule.ONCE,
                # next_run = form.cleaned_data.get("datetime").astimezone(pytz.utc),
                next_run = timezone.now() + timedelta(minutes=1),
                # minutes = int((form.cleaned_data.get("datetime").replace(tzinfo=LOCAL_TIMEZONE) - datetime.datetime.now().replace(tzinfo=LOCAL_TIMEZONE)).total_seconds()//60),
            )

            # return redirect(reverse("home"))
        
        else:
            print(form.errors)
            print(form.non_field_errors)
            form = ReminderForm()
    
    else:
        form = ReminderForm()

    return render(request, "reminder.html", context = {"form": form})