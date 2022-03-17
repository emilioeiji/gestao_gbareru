from django.db import models
from django.urls import reverse


class Posto(models.Model):
    posto = models.CharField(max_length=10)

    def __str__(self):
        return self.posto

    def get_absolute_url(self):
        return reverse('list_posto')
