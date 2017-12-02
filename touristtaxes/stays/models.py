from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    name = models.CharField(max_length=30)


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    date_begin = models.DateField()
    date_end = models.DateField()


class Stay(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    adults = models.IntegerField(default=0)
    children = models.IntegerField(default=0)
    date_begin = models.DateField()
    date_end = models.DateField()
