import streamlit as st

from health_score import calculate_health_score
from risk_predictor import predict_risks
from recommendations import generate_recommendations
from data_manager import save_user_record



st.title("🩺 Smart Health Risk Predictor")

st.write("Enter your lifestyle details to analyze your health.")

# ---- User Inputs ----
name = st.text_input("Name")
age = st.number_input("Age", 10, 100)
height = st.number_input("Height (cm)", 100.0, 220.0)
weight = st.number_input("Weight (kg)", 30.0, 150.0)
sleep = st.slider("Sleep Hours", 0.0, 12.0, 7.0)
exercise = st.selectbox("Exercise Level", ["low", "medium", "high"])
water = st.slider("Water Intake (litres)", 0.0, 5.0, 2.0)
stress = st.selectbox("Stress Level", ["low", "medium", "high"])


# ---- Analyze Button ----
if st.button("Analyze Health"):

    user = {
        "name": name,
        "age": age,
        "height": height,
        "weight": weight,
        "sleep": sleep,
        "exercise": exercise,
        "water": water,
        "stress": stress
    }

    score, bmi = calculate_health_score(user)
    risks = predict_risks(user, bmi)
    tips = generate_recommendations(user, bmi)

    save_user_record(user, score, bmi)

    st.subheader("📊 Health Results")

    st.write(f"**BMI:** {bmi:.2f}")
    st.write(f"**Health Score:** {score}/100")

    if score >= 80:
        st.success("Low Risk ✅")
    elif score >= 50:
        st.warning("Moderate Risk ⚠")
    else:
        st.error("High Risk ❌")

    st.subheader("⚠ Detected Risks")
    if len(risks) == 0:
        st.write("No major risks detected 🎉")
    else:
        for r in risks:
            st.write("⚠", r)

    st.subheader("💡 Recommendations")
    for t in tips:
        st.write("👉", t)
