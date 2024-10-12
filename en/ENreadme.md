# Real-Time Subtitles Display System Using Vosk and OpenCV

This project captures real-time audio using **PyAudio**, performs offline speech recognition with **Vosk**, and displays subtitles directly on a video captured by the webcam using **OpenCV**. The subtitles are also displayed in a second window that maintains a complete history of the recognized text.

## Features

- **Real-time audio capture** using **PyAudio**.
- **Offline speech recognition** with **Vosk**.
- **Real-time subtitles display** over the video captured by the webcam.
- **Full subtitles history display** in a separate window.

## Technologies Used

- **OpenCV**: For real-time video capture and display.
- **threading**: To run speech recognition in a separate thread, ensuring that the video is displayed without interruptions.
- **numpy**: For image matrix manipulation.
- **PyAudio**: For capturing audio from the microphone.
- **Vosk**: For offline speech recognition.
- **Pillow**: For rendering text over the video, with support for special characters and style customization.
