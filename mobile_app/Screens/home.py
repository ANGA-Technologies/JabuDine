from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Line
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivy.uix.widget import Widget
from kivymd.uix.button import MDRaisedButton, MDFlatButton


# from kivymd.uix.appbar import MDTopAppBar
from kivy.utils import get_color_from_hex

class BorderedMDCard(MDCard):
    def __init__(self, border_width=dp(2), border_color="#FF0000", **kwargs):
        super().__init__(**kwargs)
        self.border_width = border_width
        self.border_color = border_color

        # Draw the border after the background is drawn
        with self.canvas.after:
            Color(*get_color_from_hex(self.border_color))
            self.border_line = Line(width=self.border_width)

        # Keep the border updated if size or position changes
        self.bind(pos=self._update_border, size=self._update_border)

    def _update_border(self, *args):
        # For a rounded rectangle, we need (x, y, width, height, radius_top_left, ...)
        # We'll just unpack `self.radius`, which should contain 4 values.
        self.border_line.rounded_rectangle = (
            self.x,
            self.y,
            self.width,
            self.height,
            *self.radius
        )

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Float Layout for flexibility
        layout = FloatLayout()

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
                text="Your Table, Your Taste, One Tap Away!",
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
            size_hint=(1, 1), 
            size=(320, 50),  
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        # Order Button
        buttons_layout.add_widget(
            MDRaisedButton(
                text="Order",
                theme_text_color="Custom",
                text_color=get_color_from_hex("#800080"),
                md_bg_color=get_color_from_hex("#f5f5f5"),
                size_hint=(None, None),
                # size=(140, 50),
            )
        )

        # Reserve Button
        buttons_layout.add_widget(
            MDRaisedButton(
                text="Reserve",
                theme_text_color="Custom",
                text_color=get_color_from_hex("#800080"),
                md_bg_color=get_color_from_hex("#f5f5f5"),
                size_hint=(None, None),
                # size=(140, 50),
            )
        )

        layout.add_widget(buttons_layout)

        # Bottom Navigation Bar
        nav_bar = BorderedMDCard(
            orientation="horizontal",
            size_hint=(0.97, None),
            height=dp(60),
            md_bg_color=get_color_from_hex("#D9D9D94d"),
            pos_hint={"center_x": 0.5, "y": 0.01},
            padding=[dp(10), dp(10), dp(10), dp(10)],
            radius=[dp(15), dp(15), dp(15), dp(15)],  # Rounded corners
            border_width=dp(1.2),
            border_color="#D9D9D9",
        )

        # Use a BoxLayout for dynamic spacing
        icons_layout = MDBoxLayout(
            orientation="horizontal",
            size_hint=(1, 1)  # Full width to allow dynamic spacing
        )

        # Add icons with dynamic spacers between them
        icon_sources = ["home.png", "menu.png", "notification.png", "account.png"]
        for index, icon in enumerate(icon_sources):
            if index > 0:
                # Add a spacer widget between icons
                icons_layout.add_widget(Widget(size_hint_x=1))  # Spacer adjusts dynamically

            icons_layout.add_widget(FitImage(
                source=f"assets/icons/{icon}",
                size_hint=(None, None),
                size=(dp(32), dp(32))  # Fixed size for icons
            ))

        # Add the dynamic icon layout to the navigation bar
        nav_bar.add_widget(icons_layout)

        layout.add_widget(nav_bar)

        # Add the main layout to the screen
        self.add_widget(layout)
