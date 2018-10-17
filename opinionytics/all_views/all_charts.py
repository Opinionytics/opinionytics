from chartit import DataPool, Chart, PivotDataPool, PivotChart
from django.db.models import Avg

from opinionytics.models import Popularity, Polarity, Topics, Subjectivity


def all_charts(request):
    # Popularity
    # Step 1: Create a DataPool with the data we want to retrieve.
    popularity_data = \
        DataPool(
            series=[{'options': {
                'source': Popularity.objects.all()},
                'terms': [
                'concept',
                'date',
                'score']}
            ])
    # Step 2: Create the Chart object
    popularity = Chart(
        datasource=popularity_data,
        series_options=[{'options': {
            'type': 'line',
            'stacking': False},
            'terms': {
            'date': [
                'score']
        }}],
        chart_options={'title': {
            'text': ''},
            'xAxis': {
            'title': {
                'text': 'Time'}}})
    # Polarity
    # Step 1: Create a DataPool with the data we want to retrieve.
    polaritydata = PivotDataPool(
        series=[{
            'options': {
                'source': Polarity.objects.all(),
                'categories': ['confidence'],
                'legend_by': 'polarity',
                'top_n_per_cat': 3,
            },
            'terms': {
                'avg_rain': Avg('confidence'),
            }
        }]
    )
    # Step 2: Create the Chart object
    polarity = PivotChart(
        datasource=polaritydata,
        series_options=[{
            'options': {
                'type': 'column',
                'stacking': True
            },
            'terms': ['avg_rain']
        }],
        chart_options={
            'title': {
                'text': ''
            },
            'xAxis': {
                'title': {
                    'text': 'Polarity'
                },
            },
            'yAxis': {
                'title': {
                    'text': 'Confidence'
                },
                'max': 1
            }
        }
    )
    # Topics involved
    # Step 1: Create a DataPool with the data we want to retrieve.
    topicsdata = PivotDataPool(
        series=[{
            'options': {
                'source': Topics.objects.all(),
                'categories': ['confidence'],
                'legend_by': 'topics',
                'top_n_per_cat': 3,
            },
            'terms': {
                'avg_rain': Avg('confidence'),
            }
        }]
    )
    # Step 2: Create the Chart object
    topics = PivotChart(
        datasource=topicsdata,
        series_options=[{
            'options': {
                'type': 'column',
                'stacking': True
            },
            'terms': ['avg_rain']
        }],
        chart_options={
            'title': {
                'text': ' '
            },
            'xAxis': {
                'title': {
                    'text': 'Topics involved'
                },
            },
            'yAxis': {
                'title': {
                    'text': 'Confidence'
                },
                'max': 1
            }
        }
    )
    # Subjectivity
    # Step 1: Create a DataPool with the data we want to retrieve.
    subjectivitydata = PivotDataPool(
        series=[{
            'options': {
                'source': Subjectivity.objects.all(),
                'categories': ['confidence'],
                'legend_by': 'subjectivity',
                'top_n_per_cat': 3,
            },
            'terms': {
                'avg_rain': Avg('confidence'),
            }
        }]
    )
    # Step 2: Create the Chart object
    subjectivity = PivotChart(
        datasource=subjectivitydata,
        series_options=[{
            'options': {
                'type': 'column',
                'stacking': True
            },
            'terms': ['avg_rain']
        }],
        chart_options={
            'title': {
                'text': ''
            },
            'xAxis': {
                'title': {
                    'text': 'Subjectivity'
                },
            },
            'yAxis': {
                'title': {
                    'text': 'Confidence'
                },
                'max': 1
            }
        }
    )
    return [popularity, polarity, topics, subjectivity]