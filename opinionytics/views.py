from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db import connections
from django.views.generic import TemplateView
from django.db.models import Count

from chartjs.views.lines import BaseLineChartView
from chartit import DataPool, Chart
from .models import *

from opinionytics.all_views.All_features_view import *

from pytrends.request import TrendReq 
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, ConceptsOptions
from aylienapiclient import textapi

from django.db.models import Avg
from chartit import PivotDataPool, PivotChart


APP_ID = "8ebd4c0e"
APP_KEY = "707f70d4fe70e4e22210bfd824949ba9"

client = textapi.Client(APP_ID, APP_KEY)

USERNAME='ea1c5c7c-c39e-4af6-bcd5-b9103dc229a2'
PASSWORD='Xl21Xq1EeDwW'
VERSION='2017-02-27'

natural_language_understanding = NaturalLanguageUnderstandingV1(
    username=USERNAME,
    password=PASSWORD,
    version=VERSION)

pytrends = TrendReq(hl='en-US', tz=360)

all_features_view = All_features_view(client, pytrends, natural_language_understanding)

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def analyze_text(request):
    return render(request, 'analyze-text.html')


def analyze(request):
    return render(request, 'analyze.html')


def analyze_url(request):
    return render(request, 'analyze-url.html')


def analyze_data(request):
    return render(request, 'analyze-data.html')


def signup(request):
    if request.method == "POST":
        email=request.POST['email']
        password=request.POST['password']
        first_name=request.POST['firstName']
        last_name = request.POST['lastName']
        user = User.objects.create_user(email,email,password)
        user.first_name = first_name
        user.last_name = last_name
        try:
            user.save()
        except Exception as e:
            print()
            #TODO


    return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['textfield']
        password = request.POST['passwordfield']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("ok")
            return redirect("../analyze")
        # TODO
    return render(request, 'signin.html')


def signout(request):
    return render(request, 'index.html')


def get_history(request):
    return render(request, 'history.html')


def get_help(request):
    return render(request, 'help.html')


def contact(request):
    return render(request, 'contact.html')


def result(request):
    return render(request, 'result.html')


def get_result_text(request):
    if request.method == 'POST':
        text = request.POST.get('textfield', None)
        if text != None:
            if len(text.split(" ")) > 50:
                return render(request, 'result.html', all_features_view.execute_text(text))
            else:
                return HttpResponseRedirect("../analyze/")
        
        
def get_result_url(request):
    if request.method == 'POST':
        url = request.POST.get('urlfield', None)
        if url != None:
            Popularity.objects.all().delete()
            for concepts in all_features_view.execute_url(url)['popularity']:
                concept = concepts["concept"]
                for date, score in concepts["popularity"].items():
                    test = Popularity.objects.create(concept=concept, date=str(date).split()[0], score=score)
            return render(request, 'result.html', popularity_chart(request))


def get_result_data(request):
    if request.method == 'POST':
        url = request.POST.get('datafield', None)
        if url != None:
            # Todo
            # return HttpResponse(json.dumps(all_features_view.execute_data(data)), content_type="application/json")
            return


def charts(request):
    # Step 1: Create a DataPool with the data we want to retrieve.
    test = MonthlyWeatherByCity.objects.create(month = 2, boston_temp = 1.1, houston_temp = 1.1)
    test = DailyWeather.objects.create(month = 1,day = 1, temperature = 1.1, rainfall = 1.1, city = 'a', state = 'a')


    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': MonthlyWeatherByCity.objects.all()},
              'terms': [
                'month',
                'houston_temp',
                'boston_temp']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'boston_temp',
                    'houston_temp']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Weather Data of Boston and Houston'},
               'xAxis': {
                    'title': {
                       'text': 'Month number'}}})

        # Step 1: Create a PivotDataPool with the data we want to retrieve.
            
    rainpivotdata = PivotDataPool(
        series=[{
            'options': {
                'source': DailyWeather.objects.all(),
                'categories': ['month'],
                'legend_by': 'city',
                'top_n_per_cat': 3,
            },
            'terms': {
                'avg_rain': Avg('rainfall'),
            }
        }]
    )

    # Step 2: Create the PivotChart object
    rain = PivotChart(
        datasource=rainpivotdata,
        series_options=[{
            'options': {
                'type': 'column',
                'stacking': True
            },
            'terms': ['avg_rain']
        }],
        chart_options={
            'title': {
                'text': 'Rain by Month in top 3 cities'
            },
            'xAxis': {
                'title': {
                    'text': 'Month'
                }
            }
        }
    )

    # Step 3: Send the PivotChart object to the template.
    return render(request, 'test.html',
             {
                'chart_list' : [cht, rain],
             }
        )


def popularity_chart(request):
    # Step 1: Create a DataPool with the data we want to retrieve.
    popularity_data = \
        DataPool(
           series=
            [{'options': {
               'source': Popularity.objects.all()},
              'terms': [
                'concept',
                'date',
                'score']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = popularity_data,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'date': [
                    'score']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Popularity'},
               'xAxis': {
                    'title': {
                       'text': 'Time'}}})
    return {'popularity_chart' : cht}