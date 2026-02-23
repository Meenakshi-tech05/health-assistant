# risk_predictor.py

def predict_risks(user, bmi):

    risks = []

    # BMI risk
    if bmi >= 25:
        risks.append("Risk of overweight lifestyle")

    elif bmi < 18.5:
        risks.append("Risk of undernutrition")

    # Sleep risk
    if user["sleep"] < 6:
        risks.append("Sleep deficiency detected")

    # Exercise risk
    if user["exercise"] == "low":
        risks.append("Sedentary lifestyle risk")

    # Water intake risk
    if user["water"] < 1.5:
        risks.append("Dehydration risk")

    # Stress risk
    if user["stress"] == "high":
        risks.append("High stress level risk")

    return risks