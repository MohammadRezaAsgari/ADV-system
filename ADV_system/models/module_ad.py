from django.db import models
from . import *


class Ad(models.Model):
    title = models.CharField(max_length=250)
    img = models.URLField(max_length=250)
    link = models.URLField(max_length=250)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

