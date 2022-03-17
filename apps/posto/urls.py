from django.urls import path
from .views import PostoList, PostoCreate, PostoEdit, PostoDelete


urlpatterns = [
    path('', PostoList.as_view(), name='list_posto'),
    path('novo', PostoCreate.as_view(), name='create_posto'),
    path('editar/<int:pk>/', PostoEdit.as_view(), name='update_posto'),
    path('deletar/<int:pk>', PostoDelete.as_view(), name='delete_posto'),
]
