from opinionytics.features.summary.SummaryGenerator import *
from opinionytics.features.topicsInvolved.TopicClassifier import *
from opinionytics.features.positivity.PositivityAnalyzer import *
from opinionytics.features.subjectivity.SubjectivityAnalyzer import *
from opinionytics.features.popularity.PopularityAnalyzer import *
from .Analyze import Analyze


class All_features_view:
    def __init__(self, client, pytrends, natural_language_understanding):
        self.summaryGenerator = SummaryGenerator(client)
        self.subjectivityAnalyzer = SubjectivityAnalyzer(client)
        self.positivityAnalyzer = PositivityAnalyzer(client)
        self.topicsClassifier = TopicClassifier(client)
        self.popularityAnalyzer = PopularityAnalyzer(pytrends, natural_language_understanding)
    

    def __str__(self):
        return "All features view"
        

    def execute_text(self, text):
        summary = self.summaryGenerator.getSummary(text=text)
        subjectivity = self.subjectivityAnalyzer.getSubjectivity(text=text)
        positivity = self.positivityAnalyzer.getPositivity(text=text)
        topics = self.topicsClassifier.getTopics(text=text)
        popularity = self.popularityAnalyzer.getPopularity(text=text)
        analyze = Analyze(summary, subjectivity, positivity, topics, popularity)
        return analyze.get_analyze()


    def execute_url(self, url):
        summary = self.summaryGenerator.getSummary(url=url)
        subjectivity = self.subjectivityAnalyzer.getSubjectivity(url=url)
        positivity = self.positivityAnalyzer.getPositivity(url=url)
        topics = self.topicsClassifier.getTopics(url=url)
        popularity = self.popularityAnalyzer.getPopularity(url=url)
        analyze = Analyze(summary, subjectivity, positivity, topics, popularity)
        return analyze.get_analyze()

    def execute_data(self, data):
        data