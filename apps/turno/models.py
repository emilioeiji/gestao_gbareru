from django.db import models


class Turno(models.Model):
    turno = models.CharField(max_length=100, help_text="Nome do turno")

    def __str__(self):
        return self.turno
