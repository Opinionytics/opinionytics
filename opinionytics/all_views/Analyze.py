class Analyze:
    def __init__(self, summary, subjectivity, positivity, topics, popularity):
        self.summary = summary
        self.subjectivity = subjectivity
        self.positivity = positivity
        self.topics = topics
        self.popularity = popularity

    def get_analyze(self):
        analyze = {
            'summary' : self.summary,
            'subjectivity' : self.subjectivity,
            'positivity' : self.positivity,
            'topics' : self.topics,
            'popularity' : self.popularity,
        }
        return analyze