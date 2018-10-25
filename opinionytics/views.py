# Import Django packages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Import APIs packages
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from pytrends.request import TrendReq
from aylienapiclient import textapi

# Import local packages
from .api_config import *
from opinionytics.features.AllFeatures import *
from opinionytics.all_views.signin_view import signin_view
from opinionytics.all_views.signup_view import signup_view
from opinionytics.all_views.text_results_view import text_results_view
from opinionytics.all_views.url_results_view import url_results_view
from opinionytics.all_views.data_results_view import data_results_view

# Connect to the Aylien API
client = textapi.Client(TEXT_API_ID, TEXT_API_KEY)

# Connect to the NLP library
natural_language_understanding = NaturalLanguageUnderstandingV1(
    username=NLP_API_USERNAME,
    password=NLP_API_PASSWORD,
    version=NLP_API_VERSION)

# Use Google Trends API
pytrends = TrendReq(hl='en-US', tz=360)

# Get all features from the APIs
all_features = AllFeatures(
    client,
    pytrends,
    natural_language_understanding
)


# Go to the analyze view
def analyze(request):
    return render(request, 'analyze.html')


# Go to the text analyze view
def analyze_text(request):
    return render(request, 'analyze-text.html')


# Go to the data analyze view
def analyze_data(request):
    return render(request, 'analyze-data.html')


# Go to the url analyze view
def analyze_url(request):
    return render(request, 'analyze-url.html')


# Go to the index view
def index(request):
    return render(request, 'index.html')


# Go to the services view
def services(request):
    return render(request, 'services.html')


# Go to the history view
def get_history(request):
    return render(request, 'history.html')


# Go to the help view
def get_help(request):
    return render(request, 'help.html')


# Go to the contact view
def contact(request):
    return render(request, 'contact.html')


# Go to the result view
def result(request):
    return render(request, 'result.html')


# Go to the signout view
def signout(request):
    return render(request, 'index.html')


# Go to the signup view
def signup(request):
    signup_view(request)
    return render(request, 'signup.html')


# Go to the signin view
def signin(request):
    signin_view(request)
    return render(request, 'signin.html')


# Go to the get text result view
def get_result_text(request):
    text = request.POST.get('textfield', None)
    if len(text) != 0 and len(text.split(" ")) > 50:
        response = text_results_view(request, all_features)
        return render(request, 'result.html', response)
    else:
        return HttpResponseRedirect("../analyze-text")


# Go to the get url result view
def get_result_url(request):
    url = request.POST.get('urlfield', None)
    if len(url) != 0:
        response = url_results_view(request, url, all_features)
        return render(request, 'result.html', response)
    else:
        return HttpResponseRedirect("../analyze-url")


# Go to the get data result view
def get_result_data(request):
    data = request.POST.get('datafield', None)
    if len(data) != 0:
        response = data_results_view(request, data, all_features)
        return render(request, 'result.html', response)
    else:
        return HttpResponseRedirect("../analyze-data")
