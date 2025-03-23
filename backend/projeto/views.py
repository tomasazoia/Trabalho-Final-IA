from ultralytics import YOLO
import cv2
import torch
import numpy as np
import easyocr  # Biblioteca OCR
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import os

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