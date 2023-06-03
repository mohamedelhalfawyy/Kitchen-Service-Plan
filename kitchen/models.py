from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    available_days = models.ManyToManyField('Day', blank=True)

    def __str__(self):
        return self.user.username


class Day(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)
