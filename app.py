# import numpy as np
# import pandas as pd
# import pickle
# import os
# from flask import Flask, render_template, request, jsonify
# from tensorflow.keras.preprocessing import image
# from flask_cors import CORS

# # Initialize Flask App
# app = Flask(__name__)
# CORS(app)

# # Load the trained model
# with open("Model/IronDeficiency.pkl", 'rb') as file:
#     model = pickle.load(file)
# print(model.input_shape)


# # Class labels
# class_names = ['ConjunctivaAnemia', 'FingerAnemia', 'NonAnemia', 'PalmAnemia']

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return render_template('index.html')

# # Function to process and predict an image
# def predict_custom_image(model, img_path, class_names):
#     img = image.load_img(img_path, target_size=(240, 240))  # Resize image
#     img_array = image.img_to_array(img) / 255.0  # Normalize
#     img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

#     prediction = model.predict(img_array)
#     return class_names[np.argmax(prediction)]  # Get class with highest probability

# @app.route('/predict', methods=['GET', 'POST'])
# def predict():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return jsonify({'error': 'No file uploaded'}), 400

#         file = request.files['file']
        
#         if file.filename == '':
#             return jsonify({'error': 'No selected file'}), 400

#         # Save the uploaded file temporarily
#         img_path = "temp.jpg"
#         file.save(img_path)

#         # Perform prediction
#         predicted_class = predict_custom_image(model, img_path, class_names)

#         # Remove the temporary file
#         os.remove(img_path)

#     return render_template("index.html", prediction = predicted_class, img_path = img_path)

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)






import numpy as np
import os
import pickle
from flask import Flask, render_template, request, jsonify, send_from_directory
from tensorflow.keras.preprocessing import image
from flask_cors import CORS

# Initialize Flask App
app = Flask(__name__)
CORS(app)

# Load the trained model
with open("Cancer.pkl", 'rb') as file:
    model = pickle.load(file)
print(model.input_shape)

# Class labels
class_names = ['ALL', 'Brain Cancer', 'Breast Cancer', 'Cervical Cancer', 'Healthy', 'Kidney Cancer', 'Lung and Colon Cancer', 'Lymphoma', 'Oral Cancer']

# Define the temporary image directory
TEMP_DIR = 'static/temp_images'
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    img_path = None
    if request.method == 'POST':
        if 'my_image' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400

        file = request.files['my_image']

        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Save the uploaded file temporarily in the static directory
        img_path = os.path.join(TEMP_DIR, "temp.jpg")
        file.save(img_path)

        # Perform prediction
        prediction = predict_custom_image(model, img_path, class_names)

    return render_template("index.html", prediction=prediction, img_path=img_path)

# Function to process and predict an image
def predict_custom_image(model, img_path, class_names):
    img = image.load_img(img_path, target_size=(128,128))  # Resize image
    img_array = image.img_to_array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    prediction = model.predict(img_array)
    return class_names[np.argmax(prediction)]  # Get class with highest probability

# Serve the uploaded image from the static directory
@app.route('/static/temp_images/<filename>')
def serve_image(filename):
    return send_from_directory(TEMP_DIR, filename)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
