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


class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Float Layout for flexibility
        layout = FloatLayout()

        layout.add_widget(
            # theme_color = "Green",
            MDButton(
                MDButtonIcon(
                    icon="dots-horizontal",
                    color=get_color_from_hex("#ffffff"),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                ),
                style="text",
                size_hint=(None, None),
                size=(dp(15), dp(15)),
                pos_hint={"center_x": 0.9, "center_y": 0.8},
            ),
        )

        # Greeting Label
        layout.add_widget(
            MDLabel(
                adaptive_size=True,
                text="Hello, Foodie!",
                role= "large",
                font_style= "Title", 
                halign="center",
                pos_hint={"center_x": 0.3, "center_y": 0.8},
            )
        )

        # Logo/Title Label
        layout.add_widget(
            MDLabel(
                text="JabuDine",
                # font_size="32sp",
                theme_font_name="Custom",
                font_name="assets/fonts/fanfarron.otf",
                font_style="Display",
                halign="center",
                theme_text_color="Custom",
                text_color=get_color_from_hex("#965f00"),
                pos_hint={"center_x": 0.5, "center_y": 0.9},
            )
        )

        # Subtitle Label
        layout.add_widget(
            MDLabel(
                text="Your Table, Your Taste!",
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

        # Spacer Widget to center buttons
        buttons_layout.add_widget(Widget(size_hint_x=1))  # Left spacer

        # Order Button
        order_button = MDButton(
            MDButtonText(text="Order"),
        )

        # Reserve Button
        reserve_button = MDButton(
            MDButtonText(text="Reserve"),
        )

        # Add buttons to the layout
        buttons_layout.add_widget(order_button)
        buttons_layout.add_widget(reserve_button)

        # Spacer Widget to center buttons
        buttons_layout.add_widget(Widget(size_hint_x=1))  # Right spacer

        # Add the buttons layout to the main layout
        layout.add_widget(buttons_layout)


        # Add the main layout to the screen
        self.add_widget(layout)
