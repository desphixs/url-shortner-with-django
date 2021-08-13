from django.db import models


class Urls(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=100)
