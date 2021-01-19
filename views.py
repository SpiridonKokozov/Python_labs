from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Car
from django.forms import modelformset_factory
from .models import Client


class CarView(View):
    def get(self, request):
        cars = Car.objects.all()
        return render(request, "main/car_list.html", {"car_list": cars})