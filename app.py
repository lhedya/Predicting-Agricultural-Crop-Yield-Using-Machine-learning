import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# =========================================
# STYLE TAMBAHAN (CSS)
# =========================================
st.markdown("""
<style>
/* Warna box success */
.stSuccess {
    background-color: #e7f7e7 !important;
    border-left: 5px solid #2e7d32 !important;
}

/* Card Rekomendasi */
.rekom-box {
    padding: 12px;
    background-color: #f8fff4;
    border-radius: 8px;
    border-left: 4px solid #7cb342;
    margin-bottom: 8px;
}

/* Judul */
h1, h2, h3 {
    color: #2e7d32;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# =========================================
# LOAD MODEL
# =========================================
model = joblib.load("final_model.pkl")
le_fertilizer = joblib.load("le_fertilizer.pkl")
le_irrigation = joblib.load("le_irrigation.pkl")

# =========================================
# TITLE
# =========================================
st.title("🌾 Crop Yield Prediction App")
st.write("Prediksi hasil panen berdasarkan faktor lingkungan dan manajemen budidaya.")

# =========================================
# SIDEBAR INPUT
# =========================================
st.sidebar.header("🧪 Input Features")

rainfall = st.sidebar.slider("Rainfall (mm)", 0, 300, 100)
temperature = st.sidebar.slider("Temperature (°C)", 0, 50, 25)
fertilizer = st.sidebar.selectbox("Fertilizer Used", le_fertilizer.classes_)
irrigation = st.sidebar.selectbox("Irrigation Used", le_irrigation.classes_)
days = st.sidebar.slider("Days to Harvest", 30, 180, 90)

region = st.sidebar.selectbox("Region", ["North", "South", "East", "West"])
soil = st.sidebar.selectbox("Soil Type", ["Clay", "Silt", "Sandy", "Loamy", "Chalky"])
crop = st.sidebar.selectbox("Crop", ["Rice", "Wheat", "Maize", "Soybean", "Barley", "Cotton"])
weather = st.sidebar.selectbox("Weather Condition", ["Sunny", "Rainy", "Cloudy"])

predict_btn = st.sidebar.button("🌟 Predict Yield")

# =========================================
# IF BUTTON CLICKED
# =========================================
if predict_btn:
    st.subheader("📊 Hasil Prediksi Panen")

    # DataFrame input
    input_df = pd.DataFrame({
        "Rainfall_mm": [rainfall],
        "Temperature_Celsius": [temperature],
        "Fertilizer_Used": [le_fertilizer.transform([fertilizer])[0]],
        "Irrigation_Used": [le_irrigation.transform([irrigation])[0]],
        "Days_to_Harvest": [days],
        "Region": [region],
        "Soil_Type": [soil],
        "Crop": [crop],
        "Weather_Condition": [weather]
    })

    # Predict
    prediction = model.predict(input_df)[0]

    st.success(f"🌱 **Predicted Yield: {prediction:.2f} tons/hectare**")

    # =========================================
    # SIMPLE GRAPH OF INPUT FEATURES
    # =========================================
    st.subheader("📈 Visualisasi Kondisi Input")

    fig, ax = plt.subplots(figsize=(6, 3))
    sns.barplot(x=["Rainfall", "Temperature", "Days"], 
                y=[rainfall, temperature, days], 
                palette="Greens")
    plt.title("Basic Input Overview")
    st.pyplot(fig)

    # =========================================
    # REKOMENDASI
    # =========================================
    st.subheader("🌟 Rekomendasi Pertanian Otomatis")

    rekom_list = []

    # Rainfall
    if rainfall < 80:
        rekom_list.append("Irigasi perlu ditingkatkan karena curah hujan rendah.")
    elif rainfall > 200:
        rekom_list.append("Curah hujan tinggi. Perbaiki drainase untuk mencegah akar busuk.")

    # Temperature
    if temperature < 20:
        rekom_list.append("Gunakan varietas tanaman tahan dingin.")
    elif temperature > 35:
        rekom_list.append("Suhu tinggi. Gunakan mulsa atau peneduh.")

    # Soil
    if soil == "Sandy":
        rekom_list.append("Tanah berpasir: tambahkan kompos untuk meningkatkan kelembapan.")
    if soil == "Clay":
        rekom_list.append("Tanah liat: lakukan penggemburan rutin.")

    # Fertilizer
    if fertilizer in ["Low", "Minimal", "None"]:
        rekom_list.append("Tambahkan pupuk sesuai kebutuhan tanaman.")

    # Days to harvest
    if days < 60:
        rekom_list.append("Tanaman masih muda: pastikan pasokan nutrisi stabil.")

    if not rekom_list:
        rekom_list.append("Semua kondisi sudah optimal! Pertahankan perawatan tanaman.")

    # Tampilkan rekomendasi dalam card
    for r in rekom_list:
        st.markdown(f"<div class='rekom-box'>{r}</div>", unsafe_allow_html=True)
