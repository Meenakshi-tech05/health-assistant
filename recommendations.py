def generate_recommendations(user, bmi):

    tips = []


    if bmi >= 25:
        tips.append("Include 30 minutes of daily exercise.")
        tips.append("Reduce processed and sugary foods.")

    elif bmi < 18.5:
        tips.append("Increase nutritious calorie intake.")
        tips.append("Include protein-rich foods.")


    if user["sleep"] < 6:
        tips.append("Aim for 7–8 hours of sleep daily.")
        tips.append("Avoid screens 1 hour before bedtime.")

    
    if user["exercise"] == "low":
        tips.append("Start with 20–30 minutes walking daily.")

    
    if user["water"] < 1.5:
        tips.append("Drink at least 2–2.5 litres of water daily.")

    
    if user["stress"] == "high":
        tips.append("Practice meditation or breathing exercises.")
        tips.append("Take short breaks during study/work.")

    return tips