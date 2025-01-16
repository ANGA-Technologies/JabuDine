from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Line
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon, MDFabButton
from kivymd.uix.widget import MDWidget
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex


class Alerts(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Float Layout for flexibility
        layout = FloatLayout()

        layout.add_widget(
            # theme_color = "Green",
            MDFabButton(
                icon="notification-clear-all",
                style="small",
                color_map="surface",
                theme_icon_color="Custom",
                icon_color=get_color_from_hex("#4b3f2a"),
                size_hint=(None, None),
                size=(dp(15), dp(15)),
                pos_hint={"center_x": 0.9, "center_y": 0.92},
            ),
        )

        layout.add_widget(
            MDLabel(
                text="Alerts Here",
                font_size="32sp",
                halign="center",
                theme_text_color="Custom",
                text_color=get_color_from_hex("#30016D"),
                pos_hint={"center_x": 0.5, "center_y": 0.7},
            )
        )

        # Subtitle Label
        layout.add_widget(
            MDLabel(
                text="Details about Orders & Reservations made",
                font_size="18sp",
                halign="center",
                theme_text_color="Custom",
                text_color=get_color_from_hex("#800080"),
                pos_hint={"center_x": 0.5, "center_y": 0.65},
            )
        )

        # Buttons Layout
        buttons_layout = MDBoxLayout(
            orientation="horizontal",
            spacing=20,
            size_hint=(None, None),
            size=(360, 50),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        # Add the main layout to the screen
        self.add_widget(layout)
