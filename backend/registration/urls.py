from django.urls import path
from . import views
from django.contrib.auth.views import logout

urlpatterns = [
    path('login/', views.view_login, name='log'),
    path('', views.view_login, name="home"),
    path('logout/', logout, name='logout')
]