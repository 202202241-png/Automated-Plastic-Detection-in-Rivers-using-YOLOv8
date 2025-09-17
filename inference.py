from ultralytics import YOLO
import os

# Paths
MODEL_PATH = r"D:\Underwater-Waste-Detection-Using-YoloV8-And-Water-Quality-Assessment-main\models\Underwater_Waste_Detection_YoloV8\60_epochs_denoised.pt"
INPUT_DIR = "input_images"
OUTPUT_DIR = "inference_outputs"

# Create output folder if not exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load YOLOv8 model (no device here)
print(f"Loading model from: {MODEL_PATH}")
model = YOLO(MODEL_PATH)

# Run inference
results = model.predict(
    source=INPUT_DIR,
    save=True,
    project=OUTPUT_DIR,   # save results here
    name="results",       # subfolder name
    imgsz=640,
    conf=0.1,
    device="cpu"          # 👈 device set here
)

print(f"✅ Inference complete! Check results in {OUTPUT_DIR}/results/")
