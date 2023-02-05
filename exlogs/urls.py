# django import
from django.urls import path

# app import
from exlogs import views as ex_views

app_name = 'exlogs'

urlpatterns = [
    path('', ex_views.home, name='home'),
]