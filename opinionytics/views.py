from chartit import Chart, DataPool, PivotChart, PivotDataPool

from aylienapiclient import textapi
from chartjs.views.lines import BaseLineChartView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import connections
from django.db.models import Avg, Count
from django.http import (Http404, HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect, JsonResponse)
from django.shortcuts import redirect, render, render_to_response
from django.views.generic import TemplateView
from opinionytics.all_views.All_features_view import *
from pytrends.request import TrendReq
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import (ConceptsOptions,
                                                                      Features)

from .models import *

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
            analyze = all_features_view.execute_url(url)
            summary = analyze['summary']
            Popularity.objects.all().delete()
            Polarity.objects.all().delete()
            Topics.objects.all().delete()
            Subjectivity.objects.all().delete()
            polarity = analyze['positivity']
            topics = analyze['topics']
            subjectivity = analyze['subjectivity']

            for concepts in analyze['popularity']:
                concept = concepts["concept"]
                for date, score in concepts["popularity"].items():
                    Popularity.objects.create(concept=concept, date=str(date).split()[0], score=score)

            Polarity.objects.create(polarity=polarity['polarity'], confidence=polarity['polarity_confidence'])

            for concept in topics:            
                Topics.objects.create(topics=concept['label'], confidence=concept['confidence'])

            Subjectivity.objects.create(subjectivity=subjectivity['subjectivity'], confidence=subjectivity['subjectivity_confidence'])
            
            chart_list = all_charts(request)

            return render(request, 'result.html', {     
                'summary' : summary,
                'chart_list' : chart_list,
                }
            )


def get_result_data(request):
    if request.method == 'POST':
        url = request.POST.get('datafield', None)
        if url != None:
            # Todo
            # return HttpResponse(json.dumps(all_features_view.execute_data(data)), content_type="application/json")
            return

def all_charts(request):

    # Popularity

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
    popularity = Chart(
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
                   'text': 'The popularity over a period of time'},
               'xAxis': {
                    'title': {
                       'text': 'Time'}}})


    # Polarity 

    # Step 1: Create a DataPool with the data we want to retrieve.
    polaritydata = PivotDataPool(
        series=[{
            'options': {
                'source': Polarity.objects.all(),
                'categories': ['confidence'],
                'legend_by': 'polarity',
                'top_n_per_cat': 3,
            },
            'terms': {
                'avg_rain': Avg('confidence'),
            }
        }]
    )

    #Step 2: Create the Chart object
    polarity = PivotChart(
        datasource=polaritydata,
        series_options=[{
            'options': {
                'type': 'column',
                'stacking': True
            },
            'terms': ['avg_rain']
        }],
        chart_options={
            'title': {
                'text': 'Polarity of the text'
            },
            'xAxis': {
                'title': {
                    'text': 'Polarity'
                },
            },
            'yAxis': {
                'title': {
                    'text': 'Confidence'
                }
            }
        }
    )

    # Topics involved

    # Step 1: Create a DataPool with the data we want to retrieve.
    topicsdata = PivotDataPool(
        series=[{
            'options': {
                'source': Topics.objects.all(),
                'categories': ['confidence'],
                'legend_by': 'topics',
                'top_n_per_cat': 3,
            },
            'terms': {
                'avg_rain': Avg('confidence'),
            }
        }]
    )

    #Step 2: Create the Chart object
    topics = PivotChart(
        datasource=topicsdata,
        series_options=[{
            'options': {
                'type': 'column',
                'stacking': True
            },
            'terms': ['avg_rain']
        }],
        chart_options={
            'title': {
                'text': 'Topics involved in the text'
            },
            'xAxis': {
                'title': {
                    'text': 'Topics involved'
                },
            },
            'yAxis': {
                'title': {
                    'text': 'Confidence'
                }
            }
        }
    )

    # Subjectivity

    # Step 1: Create a DataPool with the data we want to retrieve.
    subjectivitydata = PivotDataPool(
        series=[{
            'options': {
                'source': Subjectivity.objects.all(),
                'categories': ['confidence'],
                'legend_by': 'subjectivity',
                'top_n_per_cat': 3,
            },
            'terms': {
                'avg_rain': Avg('confidence'),
            }
        }]
    )

    #Step 2: Create the Chart object
    subjectivity = PivotChart(
        datasource=subjectivitydata,
        series_options=[{
            'options': {
                'type': 'column',
                'stacking': True
            },
            'terms': ['avg_rain']
        }],
        chart_options={
            'title': {
                'text': 'Subjectivity of the text'
            },
            'xAxis': {
                'title': {
                    'text': 'Subjectivity'
                },
            },
            'yAxis': {
                'title': {
                    'text': 'Confidence'
                }
            }
        }
    )
 
    return [popularity, polarity, topics, subjectivity]