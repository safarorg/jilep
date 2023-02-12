from django.urls import path
from . import views

app_name = 'logs_ex'

urlpatterns = [
    path('', views.log_home, name='log_home'),
    path('add_log_ex/', views.add_log_ex, name='add_log_ex'),
    path('<int:ex_id>/', views.edit_log_ex, name='edit_log_ex'),
    path('<int:ex_id>/delete/', views.delete_log_ex, name='delete_log_ex'),
]