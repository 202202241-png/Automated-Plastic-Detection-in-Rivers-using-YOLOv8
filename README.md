# River Plastic Waste Detection using YOLOv8

## Project Overview
This project demonstrates the use of Artificial Intelligence to detect plastic waste in rivers. By implementing the YOLOv8 deep learning model, the system can accurately identify and localize plastic debris in 
real-time, providing actionable insights for cleanup efforts and pollution monitoring.

## Features
- Real-time detection of plastic waste in rivers.
-  boxes around detected plastic items with confidence scores.
- Supports images and video input.
- Helps prioritize cleanup efforts based on detected waste locations.

## Technologies Used
- *Python* – Programming language  
- *YOLOv8 (Ultralytics)* – Deep learning model for object detection  
- *OpenCV* – Image and video processing  
- *Flask– For web deployment  
- *NumPy, Pandas* – Data handling  

## How It Works
1. Input images or videos of river water are provided to the system.
2. YOLOv8 model analyzes the input and detects plastic waste like bottles, bags, and cups.
3. The system generates bounding boxes and confidence scores for each detected item.
4. Outputs can be used to guide cleanup efforts and monitor pollution levels over time.
