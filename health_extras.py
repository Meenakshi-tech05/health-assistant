# health_extras.py

def weather_health_tips(weather):

    tips = []

    if weather == "hot":
        tips.append("Drink extra water to stay hydrated.")
        tips.append("Avoid outdoor activity during peak afternoon heat.")

    elif weather == "rainy":
        tips.append("Carry an umbrella and stay dry.")
        tips.append("Maintain hygiene to avoid infections.")

    elif weather == "cold":
        tips.append("Wear warm clothing.")
        tips.append("Include warm fluids like soup or tea.")

    return tips
def habit_recommender(user):

    habits = []

    if user["sleep"] < 7:
        habits.append("Maintain a fixed sleep schedule.")

    if user["exercise"] == "low":
        habits.append("Start with 20 minutes of daily walking.")

    if user["water"] < 2:
        habits.append("Keep a water bottle nearby as a reminder.")

    if user["stress"] == "high":
        habits.append("Practice 5-minute breathing exercises daily.")

    habits.append("Include fruits and vegetables in meals.")
    habits.append("Take short breaks during long screen usage.")

    return habits