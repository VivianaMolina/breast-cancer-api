from flask import Flask, render_template, request, redirect,jsonify

import joblib
import numpy as np
import os

app = Flask(__name__, static_folder='static') 
model, target_names = joblib.load('models/model_breast_cancer.pkl')

model_path = os.path.join('models', 'model_breast_cancer.pkl')

try:
    model, target_names = joblib.load(model_path)
except FileNotFoundError:
    print(f"Model file not found at {model_path}. Please train and save the model first.")
    model, target_names = None, None  # Optional: fallback values or redirect logic

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.get_json(force=True)['features']  # Expecting a list of 30 float values
        prediction = model.predict([input_data])[0]
        label = target_names[prediction]
        return jsonify({'prediction': label})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__=="__main__":   
    app.run(debug=True)    