import cv2
import easyocr
import numpy as np

# Inicializa o leitor OCR
reader = easyocr.Reader(['en'])

def extrair_texto_da_placa(image_path):
    """Lê a imagem da placa e retorna os caracteres extraídos."""
    # Carregar a imagem
    image = cv2.imread(image_path)

    # Pré-processamento da imagem (binarização para melhor OCR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Aplicar OCR na imagem processada
    result = reader.readtext(thresh)

    # Filtrar apenas caracteres alfanuméricos válidos
    texto_detectado = ""
    for detection in result:
        texto = detection[1]  # O texto detectado está na posição 1
        texto_limpo = "".join(c for c in texto if c.isalnum())  # Remove caracteres especiais
        texto_detectado += texto_limpo

    return texto_detectado if texto_detectado else "Placa não detectada"

# Teste individual (caso queira rodar separadamente)
if __name__ == "__main__":
    placa = extrair_texto_da_placa("placa_detectada.jpg")
    print(f"Placa detectada: {placa}")
