from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarView.as_view()),
]