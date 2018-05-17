"""Opinionitycs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('index/', views.index, name='index'),

    path('about', views.about, name='about'),
    path('about/', views.about, name='about'),

    path('services', views.services, name='services'),
    path('services/', views.services, name='services'),

    path('analyze', views.analyze, name='analyze'),
    path('analyze/', views.analyze, name='analyze'),

    path('analyze-text', views.analyze_text, name='analyze-text'),
    path('analyze-text/', views.analyze_text, name='analyze-text'),

    path('analyze-url', views.analyze_url, name='analyze-url'),
    path('analyze-url/', views.analyze_url, name='analyze-url'),

    path('analyze-data', views.analyze_data, name='analyze-data'),
    path('analyze-data/', views.analyze_data, name='analyze-data'),
    
    path('signup', views.signup, name='signup'),
    path('signup/', views.signup, name='signup'),
    
    path('signin', views.signin, name='signin'),
    path('signin/', views.signin, name='signin'),
    
    path('signout', views.signout, name='signout'),
    path('signout/', views.signout, name='signout'),
    
    path('history', views.get_history, name='history'),
    path('history/', views.get_history, name='history'),
    
    path('upload', views.upload, name='upload'),
    path('upload/', views.upload, name='upload'),
    
    path('help', views.get_help, name='help'),
    path('help/', views.get_help, name='help'),

    path('get_result_text', views.get_result_text, name='result'),
    path('get_result_text/', views.get_result_text, name='result'),
    
    path('get_result_url', views.get_result_url, name='result'),
    path('get_result_url/', views.get_result_url, name='result'),

    path('contact', views.contact, name='contact'),
    path('contact/', views.contact, name='contact'),
    
    path('admin', admin.site.urls),
    path('admin/', admin.site.urls),
]
