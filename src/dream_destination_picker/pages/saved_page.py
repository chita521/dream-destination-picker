import flet as ft

def saved_page(previous_trip_text):

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Saved Trip Information",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    font_family="Playfair",
                ),

                previous_trip_text,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        ),
        padding=20,
    )