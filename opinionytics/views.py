from django.http import HttpResponseRedirect
from django.shortcuts import render

from watson_developer_cloud import NaturalLanguageUnderstandingV1
from pytrends.request import TrendReq
from aylienapiclient import textapi

from .api_config import *
from opinionytics.features.AllFeatures import *
from opinionytics.all_views.signin_view import signin_view
from opinionytics.all_views.signup_view import signup_view
from opinionytics.all_views.text_results_view import text_results_view
from opinionytics.all_views.url_results_view import url_results_view
from opinionytics.all_views.data_results_view import data_results_view

client = textapi.Client(TEXT_API_ID, TEXT_API_KEY)

natural_language_understanding = NaturalLanguageUnderstandingV1(
    username=NLP_API_USERNAME,
    password=NLP_API_PASSWORD,
    version=NLP_API_VERSION)

pytrends = TrendReq(hl='en-US', tz=360)

all_features_view = AllFeatures(
        client,
        pytrends,
        natural_language_understanding
    )

def index(request):
    return render(request, 'index.html')


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
    signup_view(request)
    return render(request, 'signup.html')


def signin(request):
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
    text = request.POST.get('textfield', None)
    if len(text) != 0 and len(text.split(" ")) > 50:
        response = text_results_view(request, all_features_view)
        return render(request, 'result.html', response)
    else:
        return HttpResponseRedirect("../analyze-text")


def get_result_url(request):
    url = request.POST.get('urlfield', None)
    if len(url) != 0:
        response = url_results_view(request, url, all_features_view)
        return render(request, 'result.html', response)
    else:
        return HttpResponseRedirect("../analyze-url")


def get_result_data(request):
    data = request.POST.get('datafield', None)
    if len(data) != 0:
        response = data_results_view(request, data, all_features_view)
        return render(request, 'result.html', response)
    else:
        return HttpResponseRedirect("../analyze-data")