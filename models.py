from django.db import models
from datetime import date
from django.urls import reverse


class Client(models.Model):
    name = models.CharField("Название", max_length=100)
    age = models.PositiveIntegerField("Возраст", default=0)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиенты"
        verbose_name_plural = "Клиенты"


class Car(models.Model):
    title = models.CharField("Название", max_length=100)
    taste = models.TextField("Описание")
    name = models.ManyToManyField(Client, verbose_name="Клиент", related_name="car_client")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("car_detail", kwage={"slug": self.url})

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"