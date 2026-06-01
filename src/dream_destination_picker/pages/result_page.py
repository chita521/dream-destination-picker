import flet as ft

def result_page(
    destination_text,
    activity_text,
    packing_text,
    destination_image,
    save_trip
):

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Your Recommendation",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    font_family="Playfair",
                ),

                destination_text,
                activity_text,
                packing_text,
                destination_image,

                ft.ElevatedButton(
                    "Save Trip",
                    icon=ft.Icons.SAVE,
                    on_click=save_trip,
                    bgcolor="#2E8B57",
                    color="white",
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        padding=30,
    )