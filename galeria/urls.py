from django.urls import path
from galeria.views import index, imagem


urlpatterns = [
    path('', index, name='index'),
    path ('image/', imagem, name='imagem'),
]
