# Breast Cancer Prediction API 

This project uses a machine learning model trained on the Breast Cancer Wisconsin dataset to classify tumors as **malignant**. It exposes a simple Flask API that accepts clinical features in JSON format and returns a prediction.  
This repository contains the necessary files to deploy a machine learning model for **Breast Cancer Prediction** using Docker Aand GitHub actions.

---

##  Model Overview

- **Dataset**: `sklearn.datasets.load_breast_cancer`
- **Model**: `RandomForestClassifier`
- **Features**: 30 clinical measurements
- **Output**: `"malignant"`

---

This repository contains the necessary files to deploy a machine learning model for **Breast Cancer Prediction** using a simple web application and Docker.

---

## Project Structure

The key files and directories are:

* **`.github/workflows`**: Contains GitHub Actions workflows, specifically `deploy.yml` for automated deployment.
* **`Documentation`**: A folder for project documentation (e.g., technical specifications, user guides).
* **`models`**: Stores the trained machine learning model files.
    * `model_breast_cancer.pkl`: The serialized (pickle) file containing the trained breast cancer classification model.
* **`breast_cancer_app.py`**: The core Python application file that loads the model and contains the logic for making predictions.
* **`server.py`**: A lightweight server (likely using Flask or FastAPI) to expose the prediction logic as a web API endpoint.
* **`Dockerfile`**: A file containing instructions to build a **Docker image** that encapsulates the application and all its dependencies.
* **`requirements.txt`**: Lists all Python dependencies required to run the application (e.g., `scikit-learn`, `flask/fastapi`, `numpy`, etc.).
* **`sample_input.json`**: An example file demonstrating the expected JSON format for an input request to the prediction API.
* **`test_request.py`**: A script to test the deployed API endpoint by sending a sample request.
* **`image.png`**: An image asset, potentially for the README or the web application itself.

---

## Getting Started

### Prerequisites

1.  **Python 3.x**
2.  **pip** (Python package installer)
3.  **Docker** (for containerized deployment)


## 🚀 How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/VivianaMolina/breast-cancer-api.git
cd breast-cancer-api

```
### 2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### 3. Train the model

```
python breast_cancer_app.py
```

### 4. Start the Flask API

```
python server.py
```

### 5. Send a test request

```
python test_request.py
```

### 6. Sample JSON Input / Ejemplo de Entrada JSON

```
{
  "features": [
    17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871,
    1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193,
    25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189
  ]
}
```

### 7. Sample Output / Ejemplo de Salid
```
{
  "prediction": "malignant"
}
```