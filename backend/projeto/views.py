import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .ocr import extrair_texto_da_placa

@csrf_exempt  # Permite requisições sem CSRF token (para testes)
def processar_imagem(request):
    """Recebe uma imagem, extrai a matrícula e retorna a resposta JSON."""
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        image_path = os.path.join("media", image.name)

        # Salvar a imagem para processamento
        with open(image_path, "wb+") as dest:
            for chunk in image.chunks():
                dest.write(chunk)

        # Processar a imagem e extrair a matrícula
        placa = extrair_texto_da_placa(image_path)

        return JsonResponse({"placa": placa, "mensagem": "Placa reconhecida com sucesso"})

    return JsonResponse({"erro": "Envie uma imagem válida"}, status=400)
