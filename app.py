import streamlit as st

from health_score import calculate_health_score
from risk_predictor import predict_risks
from recommendations import generate_recommendations
from data_manager import save_user_record
from health_extras import weather_health_tips, habit_recommender
from health_chatbot import health_chatbot


# ---------------- PAGE TITLE ----------------

st.title("🩺 Smart Health Risk Predictor")
st.write("Enter your lifestyle details to analyze your health.")


# ---------------- USER INPUTS ----------------

name = st.text_input("Name")
age = st.number_input("Age", 10, 100)
height = st.number_input("Height (cm)", 100.0, 220.0)
weight = st.number_input("Weight (kg)", 30.0, 150.0)

sleep = st.slider("Sleep Hours", 0.0, 12.0, 7.0)
exercise = st.selectbox("Exercise Level", ["low", "medium", "high"])
water = st.slider("Water Intake (litres)", 0.0, 5.0, 2.0)
stress = st.selectbox("Stress Level", ["low", "medium", "high"])

weather = st.selectbox(
    "Current Weather",
    ["hot", "rainy", "cold"]
)


# ---------------- ANALYZE BUTTON ----------------

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

    # Save user in session (IMPORTANT FOR CHATBOT)
    st.session_state["user"] = user

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

    # -------- Risks --------
    st.subheader("⚠ Detected Risks")

    if len(risks) == 0:
        st.write("No major risks detected 🎉")
    else:
        for r in risks:
            st.write("⚠", r)

    # -------- Recommendations --------
    st.subheader("💡 Recommendations")

    for t in tips:
        st.write("👉", t)

    # -------- Weather Tips --------
    weather_tips = weather_health_tips(weather)

    st.subheader("🌦 Weather-Based Health Tips")

    for tip in weather_tips:
        st.write("👉", tip)

    # -------- Habit Recommendations --------
    habits = habit_recommender(user)

    st.subheader("🥗 Healthy Habit Recommendations")

    for h in habits:
        st.write("👉", h)


# ======================================================
# 🤖 AI HEALTH ASSISTANT (OUTSIDE BUTTON — VERY IMPORTANT)
# ======================================================

st.subheader("🤖 AI Health Assistant")

# Create chat history storage
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input box
user_input = st.chat_input("Ask a health question...")

if user_input:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    # Generate assistant reply
    if "user" in st.session_state:
        reply = health_chatbot(st.session_state["user"], user_input)
    else:
        reply = "⚠ Please click **Analyze Health** first."

    # Show assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.write(reply)