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
        "image": "https://images.unsplash.com/photo-1622583529718-b68ded6804d8?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
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