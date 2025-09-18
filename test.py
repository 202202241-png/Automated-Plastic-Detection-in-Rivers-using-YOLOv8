from flask import Flask, request, render_template, send_from_directory
from ultralytics import YOLO
import os
from werkzeug.utils import secure_filename

# Paths
MODEL_PATH = r"D:\Plastic detection in rivers\models\Underwater_Waste_Detection_YoloV8\60_epochs_denoised.pt"
UPLOAD_FOLDER = "uploaded_images"
OUTPUT_FOLDER = "inference_outputs"

# Create folders if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load YOLOv8 model
print(f"Loading model from: {MODEL_PATH}")
model = YOLO(MODEL_PATH)

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Home page
@app.route('/')
def index():
    return '''
    <h2>Underwater Plastic Detection</h2>
    <form method="POST" action="/predict" enctype="multipart/form-data">
        <input type="file" name="file" accept="image/*">
        <input type="submit" value="Upload & Detect">
    </form>
    '''

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded!"
    file = request.files['file']
    if file.filename == '':
        return "No selected file!"
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    # Run YOLO inference
    results = model.predict(
        source=filepath,
        save=True,
        project=OUTPUT_FOLDER,
        name="results",
        imgsz=640,
        conf=0.1,
        device="cpu"
    )
    
    # Get the output image path
    result_image_path = os.path.join(OUTPUT_FOLDER, "results", filename)
    
    return f'''
    <h3>Detection Complete!</h3>
    <img src="/output/results/{filename}" width="640">
    <br><a href="/">Go Back</a>
    '''

# Serve output images
@app.route('/output/<path:filename>')
def output_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

# Run Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
