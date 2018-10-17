from opinionytics.models import Popularity, Polarity, Topics, Subjectivity

from opinionytics.all_views.all_charts import all_charts


def text_results_view(request, all_features_view):
        analyze = all_features_view.execute_text(text)
        summary = analyze['summary']
        Popularity.objects.all().delete()
        Polarity.objects.all().delete()
        Topics.objects.all().delete()
        Subjectivity.objects.all().delete()
        polarity = analyze['positivity']
        topics = analyze['topics']
        subjectivity = analyze['subjectivity']

        for concepts in analyze['popularity']:
            concept = concepts["concept"]
            _concept = concept
            for date, score in concepts["popularity"].items():
                Popularity.objects.create(
                    concept=concept, date=str(date).split()[0], score=score)

        Polarity.objects.create(
            polarity=polarity['polarity'], confidence=polarity['polarity_confidence'])
        _polarity = polarity = polarity['polarity']

        _topics = []
        for concept in topics:
            Topics.objects.create(
                topics=concept['label'], confidence=concept['confidence'])
            _topics.append(concept['label'])

        Subjectivity.objects.create(
            subjectivity=subjectivity['subjectivity'], confidence=subjectivity['subjectivity_confidence'])
        _subjectivity = subjectivity['subjectivity']

        chart_list = all_charts(request)

        response = {
            'concept_': _concept,
            'topics_': [t for t in _topics],
            'subjectivity_': _subjectivity,
            'polarity_': _polarity,
            'summary': summary,
            'chart_list': chart_list,
        }
        return response