import flet as ft

def home_page(
    page,
    budget_dropdown,
    weather_dropdown,
    activity_dropdown,
    generate_destination
):

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "🌎 Dream Destination Picker",
                    size=34,
                    weight=ft.FontWeight.BOLD,
                    font_family="playfair",
                    color="#0B3D91",
                ),

                ft.Text(
                    "Find the perfect destination!",
                    size=18,
                ),

                budget_dropdown,
                weather_dropdown,
                activity_dropdown,

                ft.ElevatedButton(
                    "Find Destination",
                    icon=ft.Icons.TRAVEL_EXPLORE,
                    on_click=generate_destination,
                    bgcolor="#0B3D91",
                    color="white",
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        padding=30,
    )