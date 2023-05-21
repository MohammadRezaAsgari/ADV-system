from django.db import models


class Advertiser(models.Model):
    name = models.CharField(max_length=50)
    site = models.URLField(max_length=50)
#    ads = models.ManyToManyField()

    def __str__(self):
        return self.name

