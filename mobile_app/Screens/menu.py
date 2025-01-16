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


class Menu(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Float Layout for flexibility
        layout = FloatLayout()

        layout.add_widget(
            MDFabButton(
                icon="dots-vertical",
                style="small",
                color_map="surface",
                theme_icon_color="Custom",
                icon_color=get_color_from_hex("#4b3f2a"),
                size_hint=(None, None),
                size=(dp(15), dp(15)),
                pos_hint={"center_x": 0.9, "center_y": 0.92},
            ),
        )

        # Greeting Label
        layout.add_widget(
            MDLabel(
                text="Delicious Dishes Down",
                font_size="24sp",
                halign="center",
                pos_hint={"center_x": 0.5, "center_y": 0.85},
            )
        )

        # Add the main layout to the screen
        self.add_widget(layout)
