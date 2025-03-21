from django.urls import path
from .views import processar_imagem

urlpatterns = [
    path('upload/', processar_imagem, name='upload'),  # API para upload de imagem
]
