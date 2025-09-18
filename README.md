📌 Overview

This project detects plastic waste in rivers using a pre-trained YOLOv8 model. It helps in environmental monitoring and water quality assessment.

Input images → input_images/

Load YOLOv8 model (pre-trained)

Preprocessing (resize & normalize)

CNN feature extraction

Neck (feature fusion)

Detection head (predict boxes & labels)

Post-processing (remove duplicates)

Output images saved → inference_outputs/results/

Run:-pip install ultralytics opencv-python pillow
     python main.py
