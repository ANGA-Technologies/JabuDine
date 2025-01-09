from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Line
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
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
                font_size="24sp",  # Directly specify the font size
                halign="center",
                pos_hint={"center_x": 0.5, "center_y": 0.85},
            )
        )

        # Logo/Title Label
        layout.add_widget(
            MDLabel(
                text="JabuDine",
                font_size="32sp",  # Directly specify the font size
                halign="center",
                theme_text_color="Custom",
                text_color=get_color_from_hex("#30016D"),  # Purple color
                pos_hint={"center_x": 0.5, "center_y": 0.7},
            )
        ) 
    
        

        # Subtitle Label
        layout.add_widget(
            MDLabel(
                text="Your Table, Your Taste, One Tap Away!",
                font_size="18sp",  # Directly specify the font size
                halign="center",
                theme_text_color="Custom",
                text_color=get_color_from_hex("#800080"),  # Purple color
                pos_hint={"center_x": 0.5, "center_y": 0.65},
            )
        )

        # Buttons Layout
        buttons_layout = MDBoxLayout(
            orientation="horizontal",
            spacing=20,
            size_hint=(None, None),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            width=300,
            height=50,
        )

        # Order Button
        buttons_layout.add_widget(
            MDLabel(
                text="Order",
                theme_text_color="Custom",
                text_color=get_color_from_hex("#800080"),  # Purple text
                size_hint=(0.4, None),
            )
        )

        # Reserve Button
        buttons_layout.add_widget(
            MDLabel(
                text="Reserve",
                theme_text_color="Custom",
                text_color=get_color_from_hex("#800080"),  # Purple text
                size_hint=(0.4, None),
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
            spacing=dp(10),
            radius=[dp(15), dp(15), dp(15), dp(15)],  # Rounded corners
            border_width=dp(1.2),
            border_color="#D9D9D9",
        )

        # Navigation Icons (using placeholders for simplicity)
        # nav_bar.add_widget(MDLabel(text="🏠", halign="center"))
        # nav_bar.add_widget(MDLabel(text="🍴", halign="center"))
        # nav_bar.add_widget(MDLabel(text="🔔", halign="center"))
        # nav_bar.add_widget(MDLabel(text="👤", halign="center"))

                # Navigation Icons
        nav_bar.add_widget(
            FitImage(
                source="assets/icons/home.png",
                # fit_mode="cover",  # or "contain", "fill_width", etc.
                size_hint=(None, None),
                size=(dp(32), dp(32))
            )
        )
        nav_bar.add_widget(
            FitImage(
                source="assets/icons/menu.png",
                # fit_mode="cover",
                size_hint=(None, None),
                size=(dp(32), dp(32))
            )
        )
        nav_bar.add_widget(
            FitImage(
                source="assets/icons/notification.png",
                # fit_mode="cover",
                size_hint=(None, None),
                size=(dp(32), dp(32))
            )
        )
        nav_bar.add_widget(
            FitImage(
                source="assets/icons/account.png",
                # fit_mode="cover",
                size_hint=(None, None),
                size=(dp(32), dp(32))
            )
        )

        layout.add_widget(nav_bar)

        # Add the main layout to the screen
        self.add_widget(layout)
