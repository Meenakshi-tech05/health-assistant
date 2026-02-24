

def predict_risks(user, bmi):

    risks = []

    
    if bmi >= 25:
        risks.append("Risk of overweight lifestyle")

    elif bmi < 18.5:
        risks.append("Risk of undernutrition")

    
    if user["sleep"] < 6:
        risks.append("Sleep deficiency detected")

   
    if user["exercise"] == "low":
        risks.append("Sedentary lifestyle risk")

    if user["water"] < 1.5:
        risks.append("Dehydration risk")

    if user["stress"] == "high":
        risks.append("High stress level risk")

    return risks