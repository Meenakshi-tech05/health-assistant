

import json
from datetime import datetime


FILE_NAME = "user_data.json"


def save_user_record(user, score, bmi):

    record = {
        "name": user["name"],
        "age": user["age"],
        "bmi": round(bmi, 2),
        "health_score": score,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
    except:
        data = []

    data.append(record)

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
