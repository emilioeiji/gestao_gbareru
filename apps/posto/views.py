from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from .models import Posto


class PostoCreate(CreateView):
    model = Posto
    fields = ['posto']


class PostoList(ListView):
    model = Posto


class PostoEdit(UpdateView):
    model = Posto
    fields = ['posto']


class PostoDelete(DeleteView):
    model = Posto
    success_url = reverse_lazy('list_posto')
