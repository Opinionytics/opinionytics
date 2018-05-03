class all_features_view:
    def __init__(self, summaryGenerator, subjectivityAnalyzer, positivityAnalyzer, topicsClassifier, popularityAnalyzer):
        self.summaryGenerator = summaryGenerator
        self.subjectivityAnalyzer = subjectivityAnalyzer
        self.positivityAnalyzer = positivityAnalyzer
        self.topicsClassifier = topicsClassifier
        self.popularityAnalyzer = popularityAnalyzer
    