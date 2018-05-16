from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from opinionytics.all_views.All_features_view import *

from opinionytics.features.summary.SummaryGenerator import *
from opinionytics.features.topicsInvolved.TopicClassifier import *
from opinionytics.features.positivity.PositivityAnalyzer import *
from opinionytics.features.subjectivity.SubjectivityAnalyzer import *
from opinionytics.features.popularity.PopularityAnalyzer import *

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

def input(request):
    return render(request, 'input.html')


def get_result(request):
    result_text = ""
    result_url = ""
    if request.method == 'POST':
        text = request.POST.get('textfield', None)
        url = request.POST.get('urlfield', None)
        if text != None and text != '':
            if len(text.split(" ")) > 50:
                result_text += all_features_view.execute_text(text)
                return render(request, 'result.html', {'result_text': result_text})
        else:
            return HttpResponseRedirect("../analyze/") 
        if url != None and url != '':
            result_url += all_features_view.execute_url(url)
            return render(request, 'result.html', {'result_url': result_url})
    return render("Pas de texte")
        
        
