from django.db import models


class Skill(models.Model):
    skill = models.CharField(max_length=100)

    def __str__(self):
        return self.skill
