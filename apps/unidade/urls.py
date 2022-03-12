from django.urls import path
from .views import UnidadeCreate, UnidadeEdit


urlpatterns = [
    path('novo', UnidadeCreate.as_view(), name='create_unidade'),
    path('editar/<int:pk>/', UnidadeEdit.as_view(), name='edit_unidade'),
]
