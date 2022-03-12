from django.db import models


class Unidade(models.Model):
    unidade = models.CharField(max_length=100)

    def __str__(self):
        return self.unidade

    def get_absolute_url(self):
        return reverse('home')
