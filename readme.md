# 👁️ Face Tracker System (MediaPipe + Arduino)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Arduino](https://img.shields.io/badge/Arduino-IDE-00979D?style=for-the-badge&logo=arduino)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?style=for-the-badge&logo=opencv)

Este proyecto es un sistema de seguimiento facial de dos ejes (Pan/Tilt) que utiliza **MediaPipe** para la detección de rostros en tiempo real y **Arduino** para el control físico de los servomotores.

## 🚀 Funcionalidades

* **Detección con IA:** Utiliza MediaPipe Face Detection para un rastreo fluido y preciso.
* **Selección Inteligente:** No rastrea por defecto; el usuario debe hacer **click izquierdo** sobre el rostro que desea seguir.
* **Zona de Confort (Deadzone):** Incluye un margen central de 50px para evitar vibraciones innecesarias cuando el rostro está centrado.
* **Control de Dos Ejes:** Manejo independiente de eje X (horizontal) y eje Y (vertical).

---

## 🛠️ Requisitos del Sistema

### Hardware
* **Arduino** (Uno, Nano, Mega).
* **2 Servomotores** (SG90 o similares).
* **Cámara Web**.



### Software
Instala las dependencias de Python necesarias:
```bash
pip install opencv-python mediapipe pyserial numpy