from src.features.summary.SummaryGenerator import *
from src.features.topicsInvolved.TopicClassifier import *
from src.features.positivity.PositivityAnalyzer import *
from src.features.subjectivity.SubjectivityAnalyzer import *
from src.features.popularity.PopularityAnalyzer import *



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
        result = ""
        result += str(self.subjectivityAnalyzer.getSubjectivity(text=text))
        result += str(self.positivityAnalyzer.getPositivity(text=text))
        result += str(self.topicsClassifier.getTopics(text=text))
        result += str(self.popularityAnalyzer.getPopularity(text=text))
        result += str(self.summaryGenerator.getSummary(text=text))
        return result


    def execute_url(self, url):
        result = ""
        result += str(self.subjectivityAnalyzer.getSubjectivity(url=url))
        result += str(self.positivityAnalyzer.getPositivity(url=url))
        result += str(self.topicsClassifier.getTopics(url=url))
        result += str(self.popularityAnalyzer.getPopularity(url=url))
        result += str(self.summaryGenerator.getSummary(url=url))
        return result



    def execute_data(self, data):
        data