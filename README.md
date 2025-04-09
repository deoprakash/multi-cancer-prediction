# 🔬 Cancer Prediction System

A web-based system to classify cancer types using a trained deep learning model. Built with **Flask** for server-side functionality and **Gradio** for an alternative interactive UI.

---

## 🧠 Model Overview

This project uses a trained Convolutional Neural Network (CNN) stored in `Cancer.pkl` to classify medical images into one of the following categories:

- ALL (Acute Lymphoblastic Leukemia)
- Brain Cancer
- Breast Cancer
- Cervical Cancer
- Healthy
- Kidney Cancer
- Lung and Colon Cancer
- Lymphoma
- Oral Cancer

---

## 📁 Project Structure

Cancer-Prediction-System/   
│   
├── app.py     
├── Cancer.pkl  
├── requirements.txt  
├── README.md  
├── static/  
│  └── temp_images/  
├── templates/  
│ └── index.html   


---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
- git clone https://github.com/deoprakash/cancer-prediction-system.git
- cd cancer-prediction-system   
``` 

### 2. Create Virtual Environment

### On Windows
```bash
python -m venv venv
venv\\Scripts\\activate
```

### On macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run Puthon File
```bash
python app.py
```
### 5. Access the Interfaces
```bash
Flask Web UI: http://127.0.0.1:5000
```
# 📸 Features
Upload medical image from browser

Real-time predictions with confidence score

Dual UI: HTML form (Flask) and interactive drag-drop (Gradio)

Supports 9-class cancer classification

# 📦 Dependencies
Flask  
TensorFlow / Keras  
NumPy  
Pillow    
Flask-CORS

Install with:

``` bash
pip install -r requirements.txt
```
# 🧪 Example Prediction
Upload a medical scan (e.g., MRI or histology) to see the predicted cancer class along with the confidence percentage.

# 🛡️ License

All Rights Reserved

Copyright (c) 2025 Deo Prakash

This source code is provided for educational and reference purposes only.  
You are not permitted to use, copy, modify, distribute, or sell any portion  
of this code without the express written consent of the author.

# 👨‍💻 Author
Developed by DEO PRAKASH. Contributions and feedback welcome!

## 📬 Contact

If you have any questions, suggestions, or need support, feel free to reach out:

- 📧 Email: [deoprakash364@gmail.com](mailto:deoprakash364@gmail.com)
- 💼 LinkedIn: [Deo Prakash](https://www.linkedin.com/in/deo-prakash-152265225)
- 🧑‍💻 GitHub: [deoprakash](https://github.com/deoprakash)

---
