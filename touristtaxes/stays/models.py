from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Resident(models.Model):

    class Meta:
        ordering = ['location__name', 'date_begin', 'date_end']

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_begin = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return '%s is resident of %s (from %s to %s)' % (
            self.user,
            self.location,
            self.date_begin,
            self.date_end
        )


class Stay(models.Model):

    class Meta:
        ordering = ['location__name', 'date_begin', 'date_end']

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    adults = models.IntegerField(default=0)
    children = models.IntegerField(default=0)
    date_begin = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return '%s in %s from %s to %s (%s adults, %s children)' % (
            self.user,
            self.location,
            self.date_begin,
            self.date_end,
            self.adults,
            self.children
        )
