  Real-Time Quality Control System

I developed this project during my Electrical & Electronics Engineering studies to understand the logic of industrial automation and computer vision.

  Project Goal
The aim is to analyze the live feed from a webcam to detect products that meet specific criteria (color and shape) and distinguish between "OK" (Approved) and "Defective" items in real-time.

  Technologies Used
-Python (Programming Language)
-OpenCV (Computer Vision Library)
-NumPy (Matrix Operations for Image Processing)

  How It Works?
  https://github.com/user-attachments/assets/e9cff54c-8054-4b90-869f-7a0de45e35fb
  
1. The webcam initializes when the script runs.
2. Frames are converted to HSV color space for accurate color filtering (Green in this prototype).
3. After applying morphological operations (Erosion/Dilation) to remove noise, the object is detected.
4. If the object passes the check, the system displays "PRODUCTION APPROVED" (URUN SAGLAM - ONAYLANDI) on the screen.

---
Author: Kaan Mert Toker
