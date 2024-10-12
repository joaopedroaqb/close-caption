import cv2
import threading
import numpy as np
import pyaudio
from vosk import Model, KaldiRecognizer
from PIL import Image, ImageDraw, ImageFont
import os

# Configurar o caminho para o modelo de reconhecimento de fala Vosk (chinês)
model_path = r'C:\Users\joaop\Downloads\vosk-model-small-cn-0.22\vosk-model-small-cn-0.22'

# Verifica se o caminho do modelo existe
if not os.path.exists(model_path):
    raise Exception(f"O caminho especificado para o modelo não existe: {model_path}")

# Inicializa o modelo de reconhecimento de fala do Vosk
try:
    model = Model(model_path)
    print("Modelo carregado com sucesso!")
except Exception as e:
    raise Exception(f"Erro ao carregar o modelo: {e}")

# Inicializa o reconhecedor de fala Vosk
recognizer = KaldiRecognizer(model, 16000)

# Inicializa o PyAudio para captura de áudio em tempo real
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

# Inicializa a captura de vídeo com OpenCV
cap = cv2.VideoCapture(0)

# Ajusta o tamanho da janela de vídeo
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Buffer para armazenar o texto de closed caption
caption_text = ""

# Função para desenhar texto com fundo preto usando Pillow (Fonte para suporte de chinês)
def draw_text_with_background(frame, text, position, font_size=20, text_color=(255, 255, 255), bg_color=(0, 0, 0)):
    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)
    
    font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", font_size)

    # Calcula o tamanho do texto para desenhar o fundo preto usando textbbox
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    text_x, text_y = position
    draw.rectangle([text_x, text_y, text_x + text_width + 10, text_y + text_height + 10], fill=bg_color)

    # Desenha o texto sobre o fundo preto
    draw.text((text_x + 5, text_y + 5), text, font=font, fill=text_color)
    return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

# Função para atualizar a legenda com a fala reconhecida
def update_caption():
    global caption_text
    while True:
        data = stream.read(8192, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            recognized_text = result.split('"text" : ')[-1].strip('"}\n')
            caption_text += "\n" + recognized_text  # Adiciona uma nova linha para cada nova frase reconhecida

# Inicia uma thread separada para o reconhecimento de fala
thread = threading.Thread(target=update_caption)
thread.daemon = True
thread.start()

# Loop de captura de vídeo em tempo real com exibição das legendas
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Exibe a última frase detectada diretamente no vídeo com fundo preto
    frame = draw_text_with_background(frame, caption_text.split('\n')[-1], (10, 50), font_size=20, text_color=(255, 255, 255), bg_color=(0, 0, 0))

    # Mostra o frame com a legenda em tempo real
    cv2.imshow('Video com Legenda em Tempo Real', frame)

    # Cria uma imagem maior para exibir o texto completo acumulado no quadro separado
    caption_display_frame = 255 * np.ones(shape=[800, 1200, 3], dtype=np.uint8)
    y0, dy = 20, 30
    full_lines_to_display = caption_text.split('\n')  # Exibe todas as linhas do texto acumulado
    for i, line in enumerate(full_lines_to_display[-25:]):
        caption_display_frame = draw_text_with_background(caption_display_frame, line, (10, y0 + i * dy), font_size=20, text_color=(0, 0, 0), bg_color=(255, 255, 255))

    # Mostra o bloco de texto completo acumulado no quadro separado
    cv2.imshow('Legenda Completa', caption_display_frame)

    # Sai do loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os recursos ao encerrar
cap.release()
cv2.destroyAllWindows()
stream.stop_stream()
stream.close()
audio.terminate()
