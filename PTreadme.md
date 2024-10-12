# Sistema de Exibição de Legendas em Tempo Real Usando Vosk e OpenCV

Este projeto captura áudio em tempo real usando **PyAudio**, realiza o reconhecimento de fala offline com **Vosk**, e exibe as legendas diretamente sobre um vídeo capturado pela webcam usando **OpenCV**. As legendas também são exibidas em uma segunda janela que mantém um histórico completo do texto reconhecido.

## Funcionalidades

- **Captura de áudio em tempo real** usando **PyAudio**.
- **Reconhecimento de fala offline** com **Vosk**.
- **Exibição de legendas em tempo real** sobre o vídeo capturado da webcam.
- **Exibição completa do histórico de legendas** em uma janela separada.

## Tecnologias Utilizadas

- **OpenCV**: Para captura e exibição de vídeo em tempo real.
- **threading**: Para executar o reconhecimento de fala em uma thread separada, garantindo que o vídeo seja exibido sem interrupções.
- **numpy**: Para manipulação de matrizes de imagem.
- **PyAudio**: Para captura de áudio do microfone.
- **Vosk**: Para reconhecimento de fala offline.
- **Pillow**: Para renderização de texto sobre o vídeo, com suporte a caracteres especiais e personalização de estilo.

## Estrutura do Código

### 1. Inicialização do Vosk e PyAudio

O código inicializa o modelo de reconhecimento de fala **Vosk** e configura o **PyAudio** para capturar áudio em tempo real do microfone.

```python
model_path = r'C:\Users\joaop\Downloads\vosk-model-small-pt-0.3\vosk-model-small-pt-0.3'

# Verifica se o caminho do modelo existe
if not os.path.exists(model_path):
    raise Exception(f"O caminho especificado para o modelo não existe: {model_path}")

# Inicializa o modelo de reconhecimento de fala do Vosk
model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

# Inicializa o PyAudio
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream() 
```

### 2. Captura de Vídeo
A captura de vídeo em tempo real é feita utilizando a webcam com OpenCV, ajustada para uma resolução de 1280x720 pixels. 
```python
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
```

### 3. Função de Renderização de Texto
O texto reconhecido é exibido sobre o vídeo, com fundo preto para melhorar a legibilidade, utilizando a biblioteca Pillow.
```python
def draw_text_with_background(frame, text, position, font_size=20, text_color=(255, 255, 255), bg_color=(0, 0, 0)):
    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)
    font = ImageFont.truetype("arial.ttf", font_size)
    bbox = draw.textbbox((0, 0), text, font=font)
    draw.rectangle([position[0], position[1], position[0] + bbox[2] - bbox[0] + 10, position[1] + bbox[3] - bbox[1] + 10], fill=bg_color)
    draw.text((position[0] + 5, position[1] + 5), text, font=font, fill=text_color)
    return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
```

### 4. Thread de Reconhecimento de Fala
A captura de áudio e reconhecimento de fala é feita em uma thread separada para garantir que o vídeo continue a ser exibido sem interrupções.
```python
def update_caption():
    global caption_text
    while True:
        data = stream.read(8192, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            recognized_text = result.split('"text" : ')[-1].strip('"}\n')
            caption_text += "\n" + recognized_text
```

### 5. Exibição de Vídeo e Legendas
O vídeo da câmera e as legendas são exibidos em uma janela principal. Uma segunda janela exibe o histórico completo das legendas capturadas.
```python
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Exibe a última frase detectada diretamente no vídeo
    frame = draw_text_with_background(frame, caption_text.split('\n')[-1], (10, 50), font_size=20)
    
    # Mostra o vídeo com a legenda
    cv2.imshow('Video com Legenda em Tempo Real', frame)

    # Exibe o texto completo acumulado no quadro separado
    caption_display_frame = 255 * np.ones(shape=[800, 1200, 3], dtype=np.uint8)
    y0, dy = 20, 30
    for i, line in enumerate(caption_text.split('\n')[-25:]):
        caption_display_frame = draw_text_with_background(caption_display_frame, line, (10, y0 + i * dy), font_size=20)
    
    cv2.imshow('Legenda Completa', caption_display_frame)
    
    # Sai do loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

### 6. Encerramento e Liberação de Recursos
Quando a tecla 'q' é pressionada, o programa encerra a captura de vídeo, fecha as janelas e libera os recursos de áudio e vídeo.
```python
cap.release()
cv2.destroyAllWindows()
stream.stop_stream()
stream.close()
audio.terminate()
```

## Dependências

As seguintes bibliotecas são necessárias para rodar o projeto:

- `opencv-python`: Para captura e exibição de vídeo em tempo real.
- `vosk`: Para reconhecimento de fala offline.
- `pyaudio`: Para captura de áudio em tempo real.
- `Pillow`: Para renderização de texto com suporte a caracteres especiais.
- `numpy`: Para manipulação de matrizes de imagem.

### Instalação das Dependências

Para instalar todas as dependências necessárias, execute o seguinte comando no terminal:

```bash
pip install opencv-python vosk pyaudio Pillow numpy
```