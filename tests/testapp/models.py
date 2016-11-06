from django.db import models


class Thing(models.Model):
    foo = models.CharField(max_length=10)