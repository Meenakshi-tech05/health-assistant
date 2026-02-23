# recommendations.py

def generate_recommendations(user, bmi):

    tips = []

    # BMI recommendations
    if bmi >= 25:
        tips.append("Include 30 minutes of daily exercise.")
        tips.append("Reduce processed and sugary foods.")

    elif bmi < 18.5:
        tips.append("Increase nutritious calorie intake.")
        tips.append("Include protein-rich foods.")

    # Sleep recommendations
    if user["sleep"] < 6:
        tips.append("Aim for 7–8 hours of sleep daily.")
        tips.append("Avoid screens 1 hour before bedtime.")

    # Exercise recommendations
    if user["exercise"] == "low":
        tips.append("Start with 20–30 minutes walking daily.")

    # Water intake recommendations
    if user["water"] < 1.5:
        tips.append("Drink at least 2–2.5 litres of water daily.")

    # Stress recommendations
    if user["stress"] == "high":
        tips.append("Practice meditation or breathing exercises.")
        tips.append("Take short breaks during study/work.")

    return tips