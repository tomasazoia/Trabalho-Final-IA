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
from .models import User  # Importar o modelo User


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
        # 🚨 Depuração para verificar se os dados foram recebidos corretamente
        print("Recebendo requisição POST...")

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

            if not created:
                return JsonResponse({"message": "Usuário já registrado", "nome": user.nome, "matricula": user.matricula})

            return JsonResponse({
                "message": "Usuário cadastrado com sucesso",
                "nome": user.nome,
                "matricula": user.matricula,
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