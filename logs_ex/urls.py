from django.urls import path
from . import views

app_name = 'logs_ex'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_log_ex/', views.add_log_ex, name='add_log_ex'),
    path('<int:ex_id>/', views.log_ex_detail, name='log_ex_detail'),
]