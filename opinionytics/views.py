from chartit import Chart, DataPool, PivotChart, PivotDataPool

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
from aylienapiclient import textapi

from opinionytics.all_views.signin_view import signin_view
from opinionytics.all_views.signup_view import signup_view
from .models import *

from .api_config import *

client = textapi.Client(TEXT_API_ID, TEXT_API_KEY)

natural_language_understanding = NaturalLanguageUnderstandingV1(
    username=NLP_API_USERNAME,
    password=NLP_API_PASSWORD,
    version=NLP_API_VERSION)

pytrends = TrendReq(hl='en-US', tz=360)

all_features_view = All_features_view(
    client, pytrends, natural_language_understanding)


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
        signup_view(request)
    return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        signin_view(request)
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
                analyze = all_features_view.execute_text(text)
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
                    _concept = concept
                    for date, score in concepts["popularity"].items():
                        Popularity.objects.create(
                            concept=concept, date=str(date).split()[0], score=score)

                Polarity.objects.create(
                    polarity=polarity['polarity'], confidence=polarity['polarity_confidence'])
                _polarity = polarity = polarity['polarity']

                _topics = []
                for concept in topics:
                    Topics.objects.create(
                        topics=concept['label'], confidence=concept['confidence'])
                    _topics.append(concept['label'])

                Subjectivity.objects.create(
                    subjectivity=subjectivity['subjectivity'], confidence=subjectivity['subjectivity_confidence'])
                _subjectivity = subjectivity['subjectivity']

                chart_list = all_charts(request)

                return render(request, 'result.html', {
                    'concept_': _concept,
                    'topics_': [t for t in _topics],
                    'subjectivity_': _subjectivity,
                    'polarity_': _polarity,
                    'summary': summary,
                    'chart_list': chart_list,
                }
                )
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
                _concept = concept
                for date, score in concepts["popularity"].items():
                    Popularity.objects.create(
                        concept=concept, date=str(date).split()[0], score=score)

            Polarity.objects.create(
                polarity=polarity['polarity'], confidence=polarity['polarity_confidence'])
            _polarity = polarity = polarity['polarity']

            _topics = []
            for concept in topics:
                Topics.objects.create(
                    topics=concept['label'], confidence=concept['confidence'])
                _topics.append(concept['label'])

            Subjectivity.objects.create(
                subjectivity=subjectivity['subjectivity'], confidence=subjectivity['subjectivity_confidence'])
            _subjectivity = subjectivity['subjectivity']

            chart_list = all_charts(request)

            return render(request, 'result.html', {
                'concept_': _concept,
                'topics_': [t for t in _topics],
                'subjectivity_': _subjectivity,
                'polarity_': _polarity,
                'summary': summary,
                'chart_list': chart_list,
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
            series=[{'options': {
                'source': Popularity.objects.all()},
                'terms': [
                'concept',
                'date',
                'score']}
            ])

    # Step 2: Create the Chart object
    popularity = Chart(
        datasource=popularity_data,
        series_options=[{'options': {
            'type': 'line',
            'stacking': False},
            'terms': {
            'date': [
                'score']
        }}],
        chart_options={'title': {
            'text': ''},
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

    # Step 2: Create the Chart object
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
                'text': ''
            },
            'xAxis': {
                'title': {
                    'text': 'Polarity'
                },
            },
            'yAxis': {
                'title': {
                    'text': 'Confidence'
                },
                'max': 1
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

    # Step 2: Create the Chart object
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
                'text': ' '
            },
            'xAxis': {
                'title': {
                    'text': 'Topics involved'
                },
            },
            'yAxis': {
                'title': {
                    'text': 'Confidence'
                },
                'max': 1
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

    # Step 2: Create the Chart object
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
                'text': ''
            },
            'xAxis': {
                'title': {
                    'text': 'Subjectivity'
                },
            },
            'yAxis': {
                'title': {
                    'text': 'Confidence'
                },
                'max': 1
            }
        }
    )

    return [popularity, polarity, topics, subjectivity]


def test_charts(request):
    chart_list = all_charts(request)
    return render(request, 'test.html', {
        'summary': 'Lorem ipsum',
        'chart_list': chart_list,
    }
    )
