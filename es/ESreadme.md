# Sistema de Subtítulos en Tiempo Real Usando Vosk y OpenCV

Este proyecto captura audio en tiempo real utilizando **PyAudio**, realiza el reconocimiento de voz sin conexión con **Vosk**, y muestra subtítulos directamente sobre un video capturado por la cámara web usando **OpenCV**. Los subtítulos también se muestran en una segunda ventana que mantiene un historial completo del texto reconocido.

## Funcionalidades

- **Captura de audio en tiempo real** usando **PyAudio**.
- **Reconocimiento de voz sin conexión** con **Vosk**.
- **Visualización de subtítulos en tiempo real** sobre el video capturado por la cámara web.
- **Visualización completa del historial de subtítulos** en una ventana separada.

## Tecnologías Utilizadas

- **OpenCV**: Para captura y visualización de video en tiempo real.
- **threading**: Para ejecutar el reconocimiento de voz en un hilo separado, asegurando que el video se muestre sin interrupciones.
- **numpy**: Para la manipulación de matrices de imágenes.
- **PyAudio**: Para capturar audio desde el micrófono.
- **Vosk**: Para el reconocimiento de voz sin conexión.
- **Pillow**: Para renderizar texto sobre el video, con soporte para caracteres especiales y personalización de estilo.
