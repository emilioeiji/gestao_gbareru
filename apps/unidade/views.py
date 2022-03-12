from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Unidade


class UnidadeCreate(CreateView):
    model = Unidade
    fields = ['unidade']


class UnidadeEdit(UpdateView):
    model = Unidade
    fields = ['unidade']
