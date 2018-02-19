from django.shortcuts import render

from features.summary.SummaryGenerator import *
from features.topicsInvolved.TopicClassifier import *
from features.positivity.PositivityAnalyzer import *
from features.subjectivity.SubjectivityAnalyzer import *
from aylienapiclient import textapi


APP_ID = "8ebd4c0e"
APP_KEY = "707f70d4fe70e4e22210bfd824949ba9"

client = textapi.Client(APP_ID, APP_KEY)

summaryGenerator = SummaryGenerator(client)
subjectivityAnalyzer = SubjectivityAnalyzer(client)
positivityAnalyzer = PositivityAnalyzer(client)
topicsClassifier = TopicClassifier(client)

def index(request):
    return render(request, 'input.html')

def getText(request):
    result = ""
    if request.method == 'POST':
        text = request.POST.get('textfield', None)
        result =  str(summaryGenerator.getSummary(text=text))
        result += str(subjectivityAnalyzer.getSubjectivity(text=text))
        result += str(positivityAnalyzer.getPositivity(text=text))
        result += str(topicsClassifier.getTopics(text=text))
    return render(request, 'result.html',{'result': result})
