from django.urls import path
from .views import processar_imagem, salvar_usuario_matricula, salvar_usuario, calcular_caminho, listar_viagens

urlpatterns = [
    path('upload/', processar_imagem, name='upload'),
    path("salvar_usuario_matricula/", salvar_usuario_matricula, name="salvar_usuario_matricula"), 
    path("salvar_usuario/", salvar_usuario, name="salvar_usuario"),
    path("calcular_caminho/", calcular_caminho, name="calcular_caminho"),
    path("listar_viagens/", listar_viagens, name="listar_viagens"),  # Nova rota

]
