import requests
import json

# Load sample input from JSON file
with open('sample_input.json') as f:
    data = json.load(f)

# Send POST request to Flask API
response = requests.post('http://localhost:5000/predict', json=data)

# Print the result in the console
print("🔍 Prediction Result:")
print(response.json())