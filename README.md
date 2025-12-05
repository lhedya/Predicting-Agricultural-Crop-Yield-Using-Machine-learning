# Crop Yield Prediction App 🌾

A machine learning project to predict agricultural crop yield based on environmental, soil, and crop management factors. The project includes data analysis, model development, and deployment using Streamlit.

---

## 🔍 Project Summary
This project builds a predictive model to estimate crop yield using key features such as:
- Rainfall  
- Temperature  
- Soil Type  
- Region  
- Crop Type  
- Fertilizer  
- Irrigation  
- Weather Condition  
- Days to Harvest  

After model selection, the final model and encoders are deployed in a Streamlit application.

---

## 📌 Key Steps

### 1. Exploratory Data Analysis (EDA)
- Checked missing values  
- Visualized distributions and correlations  
- Analyzed crop performance by soil, region, and weather  
- Cleaned and prepared the dataset  

### 2. Preprocessing
- Label encoding (fertilizer, irrigation)  
- One-hot encoding for categorical features  
- Scaling if needed  
- Train-test split  

### 3. Model Development
Tested models:
- Linear Regression  
- Ridge Regression  
- Lasso Regression   
- XGBoost  

Saved outputs:
- final_model.pkl  
- le_fertilizer.pkl  
- le_irrigation.pkl  

### 4. Streamlit App
The app includes:
- Input sidebar  
- Real-time prediction  
- Input visualization  
- Automated farming recommendations  
- Custom UI styling  

Main file: `app.py`

### 5. Deployment Preparation
- Created `requirements.txt`  
- Initialized Git repository  
- Pushed project to GitHub  

---

## 📁 Project Structure
│── app.py
│── final_model.pkl
│── le_fertilizer.pkl
│── le_irrigation.pkl
│── Final_Project_Data_Science.ipynb
│── requirements.txt
└── README.md


---

## 👩‍💻 Author
Lhedya Monica Ismon  
Data Analyst & Data Science Trainee – Dibimbing.id

---

