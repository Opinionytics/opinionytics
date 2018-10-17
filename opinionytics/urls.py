from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('services', views.services, name='services'),
    path('analyze', views.analyze, name='analyze'),
    path('analyze-text', views.analyze_text, name='analyze-text'),
    path('analyze-url', views.analyze_url, name='analyze-url'),
    path('analyze-data', views.analyze_data, name='analyze-data'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('history', views.get_history, name='history'),
    path('help', views.get_help, name='help'),
    path('result', views.result, name='result'),
    path('get_result_text', views.get_result_text, name='result-text'),
    path('get_result_url', views.get_result_url, name='result-url'),
    path('contact', views.contact, name='contact'),
    path('admin', admin.site.urls)
]
