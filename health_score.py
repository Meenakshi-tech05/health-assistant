def cal_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi
def bmi_score(bmi):
    if 18.5 <= bmi <= 24.9:
        return 25
    elif 25 <= bmi <= 29.9:
        return 18
    else:
        return 10

def sleep_score(hours):
    if 7 <= hours <= 9:
        return 20
    elif 5 <= hours < 7:
        return 12
    else:
        return 6


def exercise_score(level):
    if level == "high":
        return 20
    elif level == "medium":
        return 15
    else:
        return 8


def water_score(litres):
    if litres >= 2.5:
        return 15
    elif litres >= 1.5:
        return 10
    else:
        return 5


def stress_score(level):
    if level == "low":
        return 20
    elif level == "medium":
        return 12
    else:
        return 6


def calculate_health_score(user):
    bmi = cal_bmi(user["height"], user["weight"])

    total_score = (
        bmi_score(bmi)
        + sleep_score(user["sleep"])
        + exercise_score(user["exercise"])
        + water_score(user["water"])
        + stress_score(user["stress"])
    )

    return total_score, bmi