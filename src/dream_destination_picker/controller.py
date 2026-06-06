import json 
from pathlib import Path
from data import destination_data

DATA_FILE = Path("src/dream_destination_picker/data/saved_trip.json")

def get_recommendation(budget_choice, weather_choice, activity_choice):

    key = (budget_choice, weather_choice, activity_choice)

    if key in destination_data:
        return destination_data[key]

    return {
        "destination": "California",
        "activity": "Beach sightseeing",
        "packing": "Pack comfortable clothing and essentials.",
        "image": "images/maarten-van-den-heuvel-gZXx8lKAb7Y-unsplash.jpg",
    }

def save_trip_data(trip_data):

    with open(DATA_FILE, "w") as file:
        json.dump(trip_data, file)

def load_trip_data():

    if DATA_FILE.exists():

        with open(DATA_FILE, "r") as file:
            return json.load(file)

    return None

if __name__ == "__main__":

    test_data = get_recommendation(
        "Medium Budget",
        "Tropical",
        "Adventure"
    )

    print(test_data)