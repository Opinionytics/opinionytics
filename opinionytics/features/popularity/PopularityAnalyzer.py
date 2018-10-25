# Popularity

import json

# Import Watson's Services

from watson_developer_cloud.natural_language_understanding_v1 import Features, ConceptsOptions
from watson_developer_cloud import WatsonException, WatsonInvalidArgument
# Extract popularity from a text


class PopularityAnalyzer:

    def __init__(self, pytrends, natural_language_understanding):
        self.pytrends = pytrends
        self.natural_language_understanding = natural_language_understanding

    def getPopularity(self, url=None, text=None, data=None, numberConcepts=4):
        try:
            if url is not None:
                return self.__getPopularityFromUrl(url, numberConcepts=numberConcepts)
            elif text is not None:
                return self.__getPopularityFromText(text, numberConcepts=numberConcepts)
            elif data is not None:
                return self.__getPopularityFromData(data, numberConcepts=numberConcepts)
            else:
                raise ValueError('Url or text must be provided')
        except WatsonException:
            return None
        except WatsonInvalidArgument:
            return None

    def __getPopularityFromUrl(self, url, numberConcepts=4):
        concepts = self.__getConcepts(url=url, numberConcepts=numberConcepts)
        return self.__getPopularity(concepts)

    # Getting the concepts of the text
    def __getPopularityFromText(self, text, numberConcepts=4):
        concepts = self.__getConcepts(text=text, numberConcepts=numberConcepts)
        return self.__getPopularity(concepts)

    def __getConcepts(self, numberConcepts=4, min_relevance=0.75, text=None, url=None):
        response = self.natural_language_understanding.analyze(
            text=text,
            url=url,
            features=Features(concepts=ConceptsOptions(limit=numberConcepts))
        )
        concepts = response["concepts"]
        concepts = [k for k in concepts if k['relevance'] > 0.75]
        return concepts

    def __getPopularity(self, concepts):
        kw_list = [k['text'] for k in concepts]
        self.pytrends.build_payload(
            kw_list, cat=0, timeframe='today 1-m', geo='', gprop='')
        data = self.pytrends.interest_over_time()
        data = data.drop('isPartial', axis=1)
        dict_datas = data.to_dict()
        result = []
        for key, val in dict_datas.items():
            row = {}
            row["concept"] = key
            row["popularity"] = val
            result.append(row)
        return result

    def __getPopularityFromData(self, data, numberConcepts=4):
        # TODO
        result = []
        for text in data:
            result.append(self.__getPopularityFromText(
                text.get('text'), numberConcepts))

# Extract popularity from data
