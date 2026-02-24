
from health_score import calculate_health_score
from risk_predictor import predict_risks
from recommendations import generate_recommendations
from data_manager import save_user_record

def get_user_data():
    print("\n---- Smart Health Assistant ----\n")

    name = input("Enter your name: ")
    age = int(input("Age: "))
    height = float(input("Height (cm): "))
    weight = float(input("Weight (kg): "))
    sleep = float(input("Sleep hours per day: "))
    exercise = input("Exercise level (low/medium/high): ").lower()
    water = float(input("Water intake (litres/day): "))
    stress = input("Stress level (low/medium/high): ").lower()
    
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

    return user


def main():
    user = get_user_data()

    score, bmi = calculate_health_score(user)

    print(f"\nYour BMI: {bmi:.2f}")
    print(f"Health Score: {score}/100")

    if score >= 80:
        print("Risk Level: Low ✅")
    elif score >= 50:
        print("Risk Level: Moderate ⚠")
    else:
        print("Risk Level: High ❌")

    risks = predict_risks(user, bmi)

    print("\n--- Health Risks Detected ---")

    if len(risks) == 0:
        print("No major risks detected 🎉")
    else:
        for r in risks:
            print("⚠", r)
    tips = generate_recommendations(user, bmi)

    print("\n--- Personalized Recommendations ---")

    if len(tips) == 0:
        print("Great lifestyle! Keep it up 🎉")
    else:
        for t in tips:
            print("👉", t)
    save_user_record(user, score, bmi)
    print("\n✅ Health report saved successfully!")


if __name__ == "__main__":
    main()