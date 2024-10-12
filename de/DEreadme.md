# Echtzeit-Untertitel-System mit Vosk und OpenCV

Dieses Projekt erfasst Echtzeit-Audio mit **PyAudio**, führt die Offline-Spracherkennung mit **Vosk** durch und zeigt Untertitel direkt auf einem von der Webcam aufgenommenen Video mithilfe von **OpenCV** an. Die Untertitel werden auch in einem zweiten Fenster angezeigt, das den vollständigen Verlauf des erkannten Textes speichert.

## Funktionen

- **Echtzeit-Audioaufnahme** mit **PyAudio**.
- **Offline-Spracherkennung** mit **Vosk**.
- **Echtzeit-Anzeige von Untertiteln** auf dem von der Webcam aufgenommenen Video.
- **Vollständige Anzeige des Untertitelverlaufs** in einem separaten Fenster.

## Verwendete Technologien

- **OpenCV**: Für die Echtzeit-Videoaufnahme und -anzeige.
- **Threading**: Um die Spracherkennung in einem separaten Thread auszuführen, damit das Video ohne Unterbrechungen angezeigt wird.
- **numpy**: Für die Manipulation von Bildmatrizen.
- **PyAudio**: Zum Erfassen von Audio über das Mikrofon.
- **Vosk**: Für die Offline-Spracherkennung.
- **Pillow**: Zum Rendern von Text auf dem Video, mit Unterstützung für Sonderzeichen und Stiloptionen.
