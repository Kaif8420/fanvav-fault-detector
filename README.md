 PFPU Fault Detection using Machine Learning

This project demonstrates fault detection in Fan-Powered VAV Terminal Units (PFPU) using machine learning techniques and interactive dashboards.

---
 Project Overview

The model aims to classify and detect operational faults based on sensor data from simulated Fan-Powered VAV units.  
Fault types include:
- `Normal` (No fault)
- `Reheat Valve Stuck` at 0%, 50%, 80%, 100%

The pipeline includes data preprocessing, model training, evaluation, and a Streamlit dashboard for visualizing predictions.
---
Problem Statement:

HVAC systems like PFPU units often face operational faults that are hard to detect manually. These undetected faults lead to inefficiencies, discomfort, and increased maintenance costs.

---

 Solution

We developed a Random Forest Classifier that automatically identifies and classifies fault types using sensor data from simulated PFPU operations.

An interactive Streamlit dashboard  is provided for visualization and insight extraction.

---

 Project Structure

project_root/
│
├── data/
│ └── combined_pfpu_data.csv # Combined dataset used for training & dashboard
│
├── models/
│ └── random_forest_model.pkl # Saved trained model
│
├── src/
│ ├── dashboard.py # Streamlit dashboard application
│ └── fault_detector.ipynb # Jupyter Notebook for training and feature analysis
│
├── README.md # Project overview
└── requirements.txt # Python dependencies

---


---

* Dataset Notice

> ❗ **The raw and processed datasets (~2.5GB total) are not included in this repository** due to GitHub’s file size and bandwidth limitations.

- The full dataset consists of multiple time-series CSVs simulating different VAV fault conditions.
- Due to size, these files have been omitted intentionally.
- If needed, they can be shared via cloud (Google Drive, etc.) or regenerated using synthetic data scripts.

📄 What’s Included Instead

- Code is written to **handle dataset loading and labeling automatically**, once the raw CSVs are placed in the correct `data/raw/` folder.
- Placeholder `data/` folder structure is described, and scripts are modular enough to plug in your own data.

---

How to Run the Dashboard
 * currently there is an issue with the streamlit app so it will only  show column
```bash
pip install -r requirements.txt
streamlit run dashboard/dashboard.py


📊 Dashboard Features

- ✅ View sample operational data from PFPU units  
- ✅ Visualize top 10 important features affecting fault classification  
- ✅ Analyze distribution of fault types across the dataset  

Launch it with:

bash
cd src
streamlit run dashboard.py

---

 Machine Learning Model
Algorithm: RandomForestClassifier

Preprocessing: Removed NaNs, timestamps, and irrelevant columns

Target variable: fault_type

Trained on: Combined PFPU dataset (combined_pfpu_data.csv)


Installation
Install all dependencies using:

bash
Copy
Edit
pip install -r requirements.txt
Ensure you are using Python 3.8 or above.


🙋‍♂️ Author
Kaif Khan
UG GRAD & Machine Learning  Enthusiast



