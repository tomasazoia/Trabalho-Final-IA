from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=8, unique=True)  # Exemplo de matrícula
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.matricula})" 

class Viagem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    partida = models.CharField(max_length=255)
    chegada = models.CharField(max_length=255)
    data_partida = models.DateTimeField()
    data_chegada = models.DateTimeField(null=True, blank=True)
    distancia = models.FloatField(null=True, blank=True)  # Distância em km
    
    def __str__(self):
        return f"Viagem de {self.usuario.nome} de {self.partida} para {self.chegada}"

