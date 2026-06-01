import flet as ft

from controller import (
    get_recommendation,
    save_trip_data,
    load_trip_data,
)

from pages.home_page import home_page
from pages.result_page import result_page
from pages.saved_page import saved_page


def main(page: ft.Page):

    trip_data = None

    page.title = "🌎 Dream Destination Picker"

    page.window_width = 1000
    page.window_height = 750

    page.scroll = "auto"

    page.bgcolor = "#EAF6FF"

    # INPUTS

    budget_dropdown = ft.Dropdown(
        label="Budget",
        width=250,
        options=[
            ft.dropdown.Option("Low Budget"),
            ft.dropdown.Option("Medium Budget"),
            ft.dropdown.Option("Luxury Budget"),
        ],
    )

    weather_dropdown = ft.Dropdown(
        label="Weather",
        width=250,
        options=[
            ft.dropdown.Option("Warm"),
            ft.dropdown.Option("Cold"),
            ft.dropdown.Option("Tropical"),
        ],
    )

    activity_dropdown = ft.Dropdown(
        label="Activity",
        width=250,
        options=[
            ft.dropdown.Option("Adventure"),
            ft.dropdown.Option("Relaxation"),
            ft.dropdown.Option("Cultural"),
        ],
    )

    # Outputs 
    destination_text = ft.Text(size=24)
    activity_text = ft.Text(size=20)
    packing_text = ft.Text(size=18)
    previous_trip_text = ft.Text(size=18)

    destination_image = ft.Image(
        src="None",
        visible=False,
        width=500,
        height=300,
        fit="cover",
        border_radius=20,
    )

    # Functions
    def generate_destination(e):
        nonlocal trip_data
        if (
            not budget_dropdown.value
            or not weather_dropdown.value
            or not activity_dropdown.value 
        ):
            page.snack_bar = ft.SnackBar(
                ft.Text("Please select all options first!")
            )
            page.snack_bar.open = True
            page.update()
            return 

        recommendation = get_recommendation(
            budget_dropdown.value,
            weather_dropdown.value,
            activity_dropdown.value,
        )

        destination_text.value = (
            f"Destination: {recommendation['destination']}"
        )

        activity_text.value = (
            f"Activity: {recommendation['activity']}"
        )

        packing_text.value = (
            f"Packing Reminder: {recommendation['packing']}"
        )

        destination_image.src = recommendation["image"]
        destination_image.visible = True

        trip_data = recommendation

        page.update()

    def save_trip(e):

        nonlocal trip_data

        if trip_data:

            save_trip_data(trip_data)

            previous_trip_text.value = (
                f"Last Saved Destination: "
                f"{trip_data['destination']}"
            )

            page.update()

    # Load previous data
    previous_data = load_trip_data()
    
    if previous_data:
        previous_trip_text.value = (
            f"Last Saved Destination: "
            f"{previous_data['destination']}"
        )

    else:
        previous_trip_text.value = (
            "No saved trips yet."
        )

    # Pages
    home = home_page(
        page,
        budget_dropdown,
        weather_dropdown,
        activity_dropdown,
        generate_destination,
    )

    results = result_page(
        destination_text,
        activity_text,
        packing_text,
        destination_image,
        save_trip,
    )

    saved = saved_page(
        previous_trip_text
    )

    # Layout 
    page.add(
        ft.Column(
            [
                ft.Row(
                    [home, results],
                    alignment=ft.MainAxisAlignment.CENTER,
                    wrap=True,
                ),

                saved,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,
        )
    )

ft.app(target=main)