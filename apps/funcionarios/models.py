from django.db import models
from django.urls import reverse

from apps.setor.models import Setor
from apps.turno.models import Turno
from apps.grupo.models import Grupo
from apps.skill.models import Skill
from apps.unidade.models import Unidade


class Funcionario(models.Model):
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT)
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100)
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT)
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT)
    skill = models.ManyToManyField(Skill)

    def get_absolute_url(self):
        return reverse('list_funcionarios')

    def __str__(self):
        return self.nome
