from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from PIL import Image
import cv2
import json
import os
import numpy as np
import easyocr  # Biblioteca OCR
from ultralytics import YOLO
from .models import User, Viagem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Viagem, User
from datetime import datetime
from django.utils.timezone import now
from .algorithms.metodos import Grafo
from django.shortcuts import render
from django.http import JsonResponse

# Carregar o modelo treinado (substituir pelo caminho correto)
model = YOLO("../best.pt")

# Inicializar o OCR
reader = easyocr.Reader(['en'])  # 'en' para inglês, pode adicionar 'pt' se precisar

@csrf_exempt
def processar_imagem(request):
    if request.method == "POST" and request.FILES.get("image"):
        imagem = request.FILES["image"]
        image_path = "media/placa.jpg"

        # Salvar a imagem temporariamente
        with open(image_path, "wb+") as dest:
            for chunk in imagem.chunks():
                dest.write(chunk)

        # Carregar a imagem
        img = Image.open(image_path)

        # Fazer a predição com YOLO
        results = model(img)

        # Verificar se há alguma matrícula detectada
        if len(results[0].boxes) > 0:
            # Pegar a primeira matrícula detectada
            box = results[0].boxes[0].xyxy[0].cpu().numpy()  # Coordenadas [x1, y1, x2, y2]
            x1, y1, x2, y2 = map(int, box)

            # Recortar a região da matrícula
            img_cv = cv2.imread(image_path)
            cropped_plate = img_cv[y1:y2, x1:x2]

            # Salvar a imagem recortada
            cropped_plate_path = "media/placa_detectada.jpg"
            cv2.imwrite(cropped_plate_path, cropped_plate)

            # Fazer OCR na imagem recortada
            placa_texto = reader.readtext(cropped_plate, detail=0, allowlist="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", contrast_ths=0.5, adjust_contrast=0.8, add_margin=0.1)

            # Filtrar apenas letras e números válidos (removendo ruídos)
            placa_final = "".join([char for char in placa_texto if char.isalnum()])

            return JsonResponse({
                "message": "Matrícula detectada",
                "placa_texto": placa_final,  # Texto extraído da placa
                "placa_path": cropped_plate_path  # Imagem recortada
            })

        return JsonResponse({"message": "Nenhuma matrícula detectada"})

    return JsonResponse({"message": "Requisição inválida"}, status=400)

@csrf_exempt
def salvar_usuario_matricula(request):
    if request.method == "POST":
        if "image" not in request.FILES or "nome" not in request.POST:
            return JsonResponse({"message": "Imagem ou nome não encontrados no request"}, status=400)

        nome = request.POST["nome"]
        imagem = request.FILES["image"]
        image_path = "media/placa.jpg"

        # Salvar a imagem temporariamente
        try:
            with open(image_path, "wb+") as dest:
                for chunk in imagem.chunks():
                    dest.write(chunk)
        except Exception as e:
            return JsonResponse({"message": f"Erro ao salvar imagem: {str(e)}"}, status=500)

        # Carregar a imagem e fazer a predição com YOLO
        try:
            img = Image.open(image_path)
            results = model(img)

            if len(results[0].boxes) == 0:
                return JsonResponse({"message": "Nenhuma matrícula detectada"}, status=400)

            # Pegar a primeira matrícula detectada
            box = results[0].boxes[0].xyxy[0].cpu().numpy()
            x1, y1, x2, y2 = map(int, box)

            img_cv = cv2.imread(image_path)
            cropped_plate = img_cv[y1:y2, x1:x2]

            cropped_plate_path = "media/placa_detectada.jpg"
            cv2.imwrite(cropped_plate_path, cropped_plate)

            # Fazer OCR na imagem recortada
            placa_texto = reader.readtext(
                cropped_plate, detail=0, allowlist="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
                contrast_ths=0.5, adjust_contrast=0.8, add_margin=0.1
            )

            placa_final = "".join([char for char in placa_texto if char.isalnum()])

            if not placa_final:
                return JsonResponse({"message": "Não foi possível ler a matrícula corretamente"}, status=400)

            # Verificar se a matrícula já existe
            user, created = User.objects.get_or_create(
                matricula=placa_final,
                defaults={"nome": nome, "data_registro": now()}
            )

            if created:
                # Usuário foi registrado
                return JsonResponse({
                    "message": "Usuário cadastrado com sucesso",
                    "nome": user.nome,
                    "matricula": user.matricula,
                    "id": user.id,
                    "placa_path": cropped_plate_path
                })
            else:
                # Usuário já existe, faz login
                return JsonResponse({
                    "message": "Login bem-sucedido",
                    "nome": user.nome,
                    "matricula": user.matricula,
                    "id": user.id,
                    "placa_path": cropped_plate_path
                })

        except Exception as e:
            return JsonResponse({"message": f"Erro ao processar a imagem: {str(e)}"}, status=500)

    return JsonResponse({"message": "Requisição inválida"}, status=400)

@csrf_exempt
def salvar_usuario(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Pega os dados enviados no request

            nome = data.get("nome")
            matricula = data.get("matricula")

            if not nome or not matricula:
                return JsonResponse({"error": "Nome e matrícula são obrigatórios"}, status=400)

            # Verifica se a matrícula já existe
            if User.objects.filter(matricula=matricula).exists():
                return JsonResponse({"message": "Matrícula já cadastrada", "status": "exists"})

            # Se não existir, cria um novo usuário
            user = User.objects.create(nome=nome, matricula=matricula)
            return JsonResponse({"message": "Usuário cadastrado com sucesso!", "status": "created", "user_id": user.id})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Erro ao processar JSON"}, status=400)

    return JsonResponse({"error": "Método não permitido"}, status=405)

@csrf_exempt
def calcular_caminho(request):
    if request.method == "GET":
        metodo = request.GET.get('metodo')
        inicio = request.GET.get('inicio')
        destino = request.GET.get('destino')
        user_id = request.GET.get('user_id') 

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'erro': 'Usuário não encontrado'}, status=404)

        grafo = Grafo()

        if metodo == 'custo_uniforme':
            caminho, custo, nos_explorados = grafo.custo_uniforme(inicio, destino)
        elif metodo == 'aprofundamento_progressivo':
            caminho, custo, nos_explorados = grafo.aprofundamento_progressivo(inicio, destino)
        elif metodo == 'procura_sofrega':
            caminho, custo, nos_explorados = grafo.procura_sofrega(inicio, destino)
        elif metodo == 'a_estrela':
            caminho, custo, nos_explorados = grafo.a_estrela(inicio, destino)
        else:
            return JsonResponse({'erro': 'Método inválido'}, status=400)

        if not caminho:
            return JsonResponse({'erro': 'Caminho não encontrado'}, status=404)

        # Salvar a viagem na base de dados
        viagem = Viagem.objects.create(
            user=user,
            partida=inicio,
            chegada=destino,
            data_partida=now(),
            distancia=custo,
            metodo=metodo,
            caminho=caminho,
            nos_expandidos=nos_explorados
        )

        return JsonResponse({
            'metodo': metodo,
            'caminho': caminho,
            'custo': custo,
            'nos_explorados': nos_explorados,
            'viagem_id': viagem.id  # Retorna o ID da viagem criada
        })

@csrf_exempt
def listar_viagens(request):
    if request.method == "GET":
        user_id = request.GET.get('user_id')  # ID do usuário logado enviado pelo frontend

        # Verificar se o usuário existe
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'erro': 'Usuário não encontrado'}, status=404)

        # Obter todas as viagens associadas ao usuário
        viagens = Viagem.objects.filter(user=user).order_by('-data_partida')

        viagens_serializadas = [
            {
                "id": viagem.id,
                "partida": viagem.partida,
                "chegada": viagem.chegada,
                "data_partida": viagem.data_partida.strftime('%Y-%m-%d %H:%M:%S'),
                "data_chegada": viagem.data_chegada.strftime('%Y-%m-%d %H:%M:%S') if viagem.data_chegada else None,
                "distancia": viagem.distancia,
                "metodo": viagem.metodo,
                "caminho": viagem.caminho,
                "nos_expandidos": viagem.nos_expandidos,
            }
            for viagem in viagens
        ]

        return JsonResponse({"viagens": viagens_serializadas}, status=200)

    return JsonResponse({"erro": "Método não permitido"}, status=405)