# Système de Sous-titres en Temps Réel Utilisant Vosk et OpenCV

Ce projet capture l'audio en temps réel à l'aide de **PyAudio**, effectue la reconnaissance vocale hors ligne avec **Vosk**, et affiche les sous-titres directement sur une vidéo capturée par la webcam à l'aide de **OpenCV**. Les sous-titres sont également affichés dans une deuxième fenêtre qui conserve un historique complet du texte reconnu.

## Fonctionnalités

- **Capture audio en temps réel** avec **PyAudio**.
- **Reconnaissance vocale hors ligne** avec **Vosk**.
- **Affichage des sous-titres en temps réel** sur la vidéo capturée par la webcam.
- **Affichage complet de l'historique des sous-titres** dans une fenêtre séparée.

## Technologies Utilisées

- **OpenCV** : Pour la capture et l'affichage de vidéo en temps réel.
- **threading** : Pour exécuter la reconnaissance vocale dans un thread séparé, garantissant que la vidéo soit affichée sans interruptions.
- **numpy** : Pour la manipulation des matrices d'images.
- **PyAudio** : Pour capturer l'audio à partir du microphone.
- **Vosk** : Pour la reconnaissance vocale hors ligne.
- **Pillow** : Pour afficher du texte sur la vidéo, avec prise en charge des caractères spéciaux et personnalisation du style.
