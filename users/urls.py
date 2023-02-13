from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('register/', views.register, name="register"),
]