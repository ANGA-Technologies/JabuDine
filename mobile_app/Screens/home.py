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
        # self.theme_cls.primary_palette = "Purple"

        # Float Layout for flexibility
        layout = FloatLayout()

        layout.add_widget(
            # theme_color = "Green",
            MDFabButton(
                icon="account",
                style="small",
                color_map="tertiary",
                # theme_icon_color="Custom",
                icon_color=get_color_from_hex("#ffffff"),
                size_hint=(None, None),
                size=(dp(15), dp(15)),
                pos_hint={"center_x": 0.9, "center_y": 0.92},
            ),
                # pos_hint={"center_x": 0.9, "center_y": 0.95},
        )

        # Greeting Label
        layout.add_widget(
            MDLabel(
                text="Hello, Happy!",
                font_size="24sp",
                halign="center",
                pos_hint={"center_x": 0.5, "center_y": 0.85},
            )
        )

        # Logo/Title Label
        layout.add_widget(
            MDLabel(
                text="JabuDine",
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

        # Bottom Navigation Bar using MDCard
        nav_bar = MDCard(
            style="filled",
            theme_bg_color= "Custom",
            md_bg_color= get_color_from_hex("#ffffff50"),
            orientation="horizontal",
            size_hint=(0.97, None),
            height=dp(60), 
            # md_bg_color=get_color_from_hex("#000000"),
            pos_hint={"center_x": 0.5, "y": 0.01},
            padding=[dp(25), dp(10), dp(25), dp(10)],
            # radius=[dp(15), dp(15), dp(15), dp(15)],  # Rounded corners
            # elevation=8,  # Add elevation for a shadow effect
        )

        # Use a BoxLayout for dynamic spacing
        icons_layout = MDBoxLayout(
            orientation="horizontal",
            size_hint=(1, 1), 
            height=dp(60),
        )

        # Add icons with dynamic spacers between them
        icon_sources = ["home", "silverware-variant", "bell", "bookmark-multiple"]
        for index, icon in enumerate(icon_sources):
            if index > 0:
                # Add a spacer widget between icons
                icons_layout.add_widget(Widget(size_hint_x=1))  # Spacer adjusts dynamically

            # Check if the current icon is "home" to set the style
            # button_style = "elevated" if icon == "home" else "filled"
            if icon == "home":
                button_style = "elevated"
            else:
                button_style = "filled"

            icons_layout.add_widget(MDButton(
                MDButtonIcon(
                    icon=icon,
                    size_hint=(None, None),
                    size=(dp(32), dp(32)),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                ),
                style=button_style,
                size_hint=(None, None),
                size=(dp(32), dp(32)),
                pos_hint={"center_x": 0.5, "center_y": 0.5}
            ))

        # Add the dynamic icon layout to the navigation bar
        nav_bar.add_widget(icons_layout)

        # Add the navigation bar to the main layout
        layout.add_widget(nav_bar)

        # Add the main layout to the screen
        self.add_widget(layout)
