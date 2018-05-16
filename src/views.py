from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from src.all_views.All_features_view import *

from pytrends.request import TrendReq 
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, ConceptsOptions
from aylienapiclient import textapi



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


def analyze_text(request):
    return render(request, 'analyze-text.html')


def analyze_url(request):
    return render(request, 'analyze-url.html')


def signup(request):
    return render(request, 'signup.html')


def signin(request):
    return render(request, 'signin.html')


def signout(request):
    return render(request, 'index.html')


def get_history(request):
    return render(request, 'history.html')


def upload(request):
    return render(request, 'upload.html')


def get_help(request):
    return render(request, 'help.html')


def get_result_text(request):
    if request.method == 'POST':
        text = request.POST.get('textfield', None)
        
        if text != None:
            if len(text.split(" ")) > 50:
                return render(request, 'result.html', {'result': all_features_view.execute_text(text)})
            else:
                return HttpResponseRedirect("../analyze/")
        
        
def get_result_url(request):
    if request.method == 'POST':
        url = request.POST.get('urlfield', None)
        if url != None:
            return render(request, 'result.html', {'result': all_features_view.execute_url(url)})
