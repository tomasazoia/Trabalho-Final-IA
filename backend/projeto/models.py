from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=8, unique=True)  # Exemplo de matrícula
    data_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        app_label = "projeto"  

    def __str__(self):
        return f"{self.nome} ({self.matricula})" 

class Viagem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    partida = models.CharField(max_length=255)
    chegada = models.CharField(max_length=255)
    data_partida = models.DateTimeField()
    data_chegada = models.DateTimeField(null=True, blank=True)
    distancia = models.FloatField(null=True, blank=True)
    metodo = models.CharField(null=True, max_length=50, choices=[
        ('custo_uniforme', 'Custo Uniforme'),
        ('profundidade', 'Aprofundamento Progressivo'),
        ('sofrega', 'Procura Sofrega'),
        ('a_estrela', 'A*')
    ])
    caminho = models.JSONField(null=True, blank=True)
    nos_expandidos = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label = "projeto" 
    
    def __str__(self):
        return f"Viagem de {self.user.nome} de {self.partida} para {self.chegada} ({self.metodo})"

