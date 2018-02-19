from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='input'),
    path('getText/', views.getText, name='getText'),
]