# Topics Involved Feature
# Classifying text from a string input

# Import NLP library
from watson_developer_cloud.natural_language_understanding_v1 import Features, ConceptsOptions


class TopicClassifier:
    def __init__(self, pytrends, natural_language_understanding):
        self.pytrends = pytrends
        self.natural_language_understanding = natural_language_understanding

    # Getting concepts from url and text
    def getTopics(self, numberConcepts=4, min_relevance=0.75, text=None, url=None):
        response = self.natural_language_understanding.analyze(
            text=text,
            url=url,
            features=Features(concepts=ConceptsOptions(limit=numberConcepts))
        )
        concepts = response["concepts"]
        concepts = [{'label': k['text'], 'confidence': k['relevance']}
                    for k in concepts]
        return concepts

    # Classifying data from a file input
    def __classifyData(self, data):
        # TODOs
        pass
