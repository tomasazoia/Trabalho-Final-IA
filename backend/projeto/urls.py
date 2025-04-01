from django.urls import path
from .views import processar_imagem, salvar_usuario_matricula, salvar_usuario

urlpatterns = [
    path('upload/', processar_imagem, name='upload'),
    path("salvar_usuario_matricula/", salvar_usuario_matricula, name="salvar_usuario_matricula"), 
    path("salvar_usuario/", salvar_usuario, name="salvar_usuario")
]
