# 🌾 Crop Yield Prediction App

A machine learning project for predicting agricultural crop yield based on environmental, soil, and crop management factors. This project includes end-to-end data processing, from EDA, preprocessing, model development, evaluation, and deployment using Streamlit.

---

## 🔍 Project Overview
This project aims to build a predictive system that estimates crop yield using key agricultural factors such as:

- Rainfall
- Temperature
- Soil Type
- Region
- Crop Type
- Fertilizer Used
- Irrigation Used
- Weather Condition
- Days to Harvest

The final model is deployed through an interactive Streamlit application.

---

## 📊 Workflow Summary

### 1. Exploratory Data Analysis (EDA)
- Checked missing values
- Analyzed distributions and data patterns
- Explored relationships between weather, soil, region, and crop yield
- Outlier detection and cleaning

### 2. Data Preprocessing
- Label Encoding for:
  - Fertilizer
  - Irrigation
- One-hot encoding for categorical variables
- Normalization / scaling (if required)
- Train-test split

### 3. Model Development
Models evaluated:
- Linear Regression
- Ridge Regression
- Lasso Regression
- XGBoost

Saved models:
- final_model.pkl
- le_fertilizer.pkl
- le_irrigation.pkl

### 4. Streamlit Application
Features:
- Sidebar input form
- Real-time yield prediction
- Input visualization
- Automatic agriculture recommendations
- Modern UI with custom CSS

Main application file: app.py

### 5. Deployment Setup
- Created requirements.txt
- Initialized Git repository
- Uploaded project to GitHub

---

## 📁 Project Structure

---

## 👩‍💻 Author
Lhedya Monica Ismon  
Data Analyst & Data Science Trainee — Dibimbing.id
GitHub: https://github.com/lhedya
