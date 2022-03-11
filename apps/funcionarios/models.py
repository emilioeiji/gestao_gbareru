from django.db import models
from apps.setor.models import Setor
from apps.turno.models import Turno
from apps.grupo.models import Grupo
from apps.skill.models import Skill


class Funcionario(models.Model):
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100)
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT)
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT)
    skill = models.ManyToManyField(Skill)

    def __str__(self):
        return self.nome
