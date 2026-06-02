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

    page.fonts = {
        "Antic": "/Users/akhilachitluri/Documents/GitHub/dream-destination-picker/src/dream_destination_picker/fonts/Antic-Regular.ttf",
        "Playfair": "/Users/akhilachitluri/Documents/GitHub/dream-destination-picker/src/dream_destination_picker/fonts/PlayfairDisplay-VariableFont_wght.ttf",
    }

    page.theme = ft.Theme(font_family="Antic")

    # SNACKBAR
    page.error_snack = ft.SnackBar(
        content=ft.Text(
            "⚠️ Please select all options first!",
            color="white",
        ),
        bgcolor="red",
    )
    #page.show_dialog(page.error_snack)

    # DROPDOWNS (INPUTS)
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

    # OUTPUT ELEMENTS
    destination_text = ft.Text(size=24)
    activity_text = ft.Text(size=20)
    packing_text = ft.Text(size=18)
    previous_trip_text = ft.Text(size=18)

    destination_image = ft.Image(
        src=None,
        visible=False,
        width=500,
        height=300,
        fit="cover",
        border_radius=20,
    )

    # PAGE NAVIGATION FUNCTIONS
    def show_home():

        # RESET DROPDOWNS 
        budget_dropdown.value = None
        weather_dropdown.value = None 
        activity_dropdown.value = None

        page.clean()

        page.add(
            home_page(
                page,
                budget_dropdown,
                weather_dropdown,
                activity_dropdown,
                generate_destination,
            )
        )
        page.update()

    def show_result():
        page.clean()
        page.add(results)

    def show_saved():
        page.clean()
        page.add(saved)

    # LOGIC FUNCTIONS
    def generate_destination(e):
        nonlocal trip_data

        if (
            not budget_dropdown.value
            or not weather_dropdown.value
            or not activity_dropdown.value
        ):
            if not page.error_snack.open:
                page.show_dialog(page.error_snack)
                #page.update()
            return

        recommendation = get_recommendation(
            budget_dropdown.value,
            weather_dropdown.value,
            activity_dropdown.value,
        )

        destination_text.value = f"Destination: {recommendation['destination']}"
        activity_text.value = f"Activity: {recommendation['activity']}"
        packing_text.value = f"Packing Reminder: {recommendation['packing']}"

        destination_image.src = recommendation["image"]
        destination_image.visible = True

        trip_data = recommendation

        page.update()

        show_result() 

    def save_trip(e):
        nonlocal trip_data

        if trip_data:
            save_trip_data(trip_data)

            previous_trip_text.value = (
                f"Last Saved Destination: {trip_data['destination']}"
            )

            page.update()

            show_saved() 

    # LOAD SAVED DATA
    previous_data = load_trip_data()

    if previous_data:
        previous_trip_text.value = (
            f"Last Saved Destination: {previous_data['destination']}"
        )
    else:
        previous_trip_text.value = "No saved trips yet."

    # BUILD PAGES
    home = home_page(
        page,
        budget_dropdown,
        weather_dropdown,
        activity_dropdown,
        generate_destination,
    )

    results = ft.Column(
        [
            result_page(
                destination_text,
                activity_text,
                packing_text,
                destination_image,
                save_trip,
            ),

            ft.Row(
                [
                    ft.ElevatedButton(
                        "Try Again",
                        on_click=lambda e: show_home(),
                        bgcolor="#0B3D91",
                        color="white",
                    ),
                    ft.ElevatedButton(
                        "View Saved Trips",
                        on_click=lambda e: show_saved(),
                        bgcolor="#0B3D91",
                        color="white",
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    saved = ft.Column(
        [
            saved_page(previous_trip_text),

            ft.ElevatedButton(
                "Plan Another Trip",
                on_click=lambda e: show_home(),
                bgcolor="#0B3D91",
                color="white",
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # START APP ON HOME PAGE
    show_home()


ft.app(target=main)