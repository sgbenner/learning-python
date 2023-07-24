import os
import requests

NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_URL =  os.environ.get("SHEETY_URL")

def get_exercise_details(exercise_desc):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_API_KEY,
        "x-remote-user-id": "0"
    }

    url = "https://trackapi.nutritionix.com/v2/natural/exercise"

    params = {
        "query": exercise_desc,
        "gender": "male",
        "weight_kg": 68,
        "height_cm": 178,
        "age": 35
    }

    response = requests.post(url=url, headers=headers, data=params)
    response.raise_for_status()

    return response.json()


def get_workouts():
    headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }
    response = requests.get(url=SHEETY_URL,
                            headers=headers)
    response.raise_for_status()

    return response.json()


def add_workout(exercise, duration, calories, input):
    url = SHEETY_URL
    params = {
        "workout": {
            "date": "2023-07-24",
            "time": "9am",
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
            "input": input
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }

    response = requests.post(url, json=params, headers=headers)
    response.raise_for_status()
    return response.json()


# do things
exercise_desc = input("What exercise did you complete? ")

results = get_exercise_details(exercise_desc=exercise_desc)

for exercise in results["exercises"]:
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    user_input = exercise["user_input"]

    add_workout(exercise=user_input, duration=duration, calories=calories, input=exercise_desc)
