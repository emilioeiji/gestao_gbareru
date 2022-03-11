from django.db import models


class Grupo(models.Model):
    grupo = models.CharField(max_length=1)

    def __str__(self):
        return self.grupo
