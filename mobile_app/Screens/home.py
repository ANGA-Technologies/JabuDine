from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.appbar import MDTopAppBar


class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Float Layout for flexibility
        layout = FloatLayout()

        # Top Bar
        top_bar = MDTopAppBar(
            pos_hint={"center_x": 0.5, "top": 1},
            elevation=4,
        )
        top_bar.title = "Home"
        self.add_widget(top_bar)

        # Greeting Label
        layout.add_widget(
            MDLabel(
                text="Hello, Happy!",
                # font_style="H5",
                halign="center",
                pos_hint={"center_x": 0.5, "center_y": 0.85},
            )
        )

        # Logo/Title Label
        layout.add_widget(
            MDLabel(
                text="JabuDine",
                # font_style="H4",
                halign="center",
                theme_text_color="Custom",
                text_color=(0.5, 0, 0.5, 1),  # Purple
                pos_hint={"center_x": 0.5, "center_y": 0.7},
            )
        )

        # Subtitle Label
        layout.add_widget(
            MDLabel(
                text="Your Table, Your Taste, One Tap Away!",
                # font_style="Subtitle2",
                halign="center",
                theme_text_color="Custom",
                text_color=(0.5, 0, 0.5, 1),  # Purple
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

        # # Order Button
        # buttons_layout.add_widget(
        #     MDButton(
        #         text="Order",
        #         text_color=(0.5, 0, 0.5, 1),  # Purple text
        #         size_hint=(0.4, None),
        #         md_bg_color=(1, 1, 1, 1),  # White background
        #         elevation=3,
        #     )
        # )

        # Reserve Button
        # buttons_layout.add_widget(
        #     MDButton(
        #         MDButtonText(
        #             text="Reserve",
        #         ),
        #         text_color=(0.5, 0, 0.5, 1),  # Purple text
        #         size_hint=(0.4, None),
        #         md_bg_color=(1, 1, 1, 1),  # White background
        #         elevation=3,
        #     )
        # )

        # layout.add_widget(buttons_layout)

        # Bottom Navigation Bar
        nav_bar = MDBoxLayout(
            orientation="horizontal",
            size_hint=(1, None),
            height=60,
            md_bg_color=(0.9, 0.6, 0, 1),  # Orange background
            pos_hint={"center_x": 0.5, "y": 0},
        )

        # Navigation Icons
        # nav_bar.add_widget(MDButton(text="🏠", md_bg_color=(0.9, 0.6, 0, 1)))
        # nav_bar.add_widget(MDButton(text="🍴", md_bg_color=(0.9, 0.6, 0, 1)))
        # nav_bar.add_widget(MDButton(text="🔔", md_bg_color=(0.9, 0.6, 0, 1)))
        # nav_bar.add_widget(MDButton(text="👤", md_bg_color=(0.9, 0.6, 0, 1)))

        layout.add_widget(nav_bar)

        # Add the main layout to the screen
        self.add_widget(layout)
