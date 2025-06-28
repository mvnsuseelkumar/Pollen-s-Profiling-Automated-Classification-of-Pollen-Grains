import numpy as np
import pandas as pd
import os
import pickle
import tensorflow as tf
from flask import Flask, request, render_template,jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Set the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model (corrected path)
model = load_model(os.path.join(BASE_DIR, 'pollen_model.keras'), compile=False)

# Load label encoder (corrected path)
with open(os.path.join(BASE_DIR, "labelencoder.pkl"), "rb") as f:
    le = pickle.load(f)

class_names = le.classes_.tolist()

# prediction function
def predict_image_class(model, img_path, target_size=(128, 128)):
    img = load_img(img_path, target_size=target_size)
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction_img = model.predict(img_array, verbose=0)
    predicted_index = np.argmax(prediction_img, axis=1)[0]
    predicted_label = class_names[predicted_index]

    return predicted_index, predicted_label



# flask app
app = Flask(__name__,template_folder='templates', static_folder='static')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/prediction')
def prediction():
    return render_template('prediction.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/predict',methods=['POST'])
def predict_api():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if not file:
        return jsonify({"error": "Empty file"}), 400

    # Save file to uploads folder
    uploads_path = os.path.join(BASE_DIR, "uploads")
    os.makedirs(uploads_path, exist_ok=True)  # Ensure the folder exists

    file_path = os.path.join(uploads_path, file.filename)
    file.save(file_path)

    index, label = predict_image_class(model, file_path)

    return jsonify({
        "class_index": int(index),
        "class_label": label
    })

# Run App
if __name__ == "__main__":
    app.run(debug=True)
