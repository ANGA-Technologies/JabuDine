import os
import sqlite3
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDButton, MDIconButton
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.fitimage import FitImage


class Explore(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Fetch restaurants from the database
        def fetch_restaurants_from_db():
            db_path = os.path.join("assets", "db", "jabudine.db")  # Correct path
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Fetch restaurant data
            cursor.execute("SELECT name, img, location FROM restaurants")
            restaurants = cursor.fetchall()

            conn.close()
            return restaurants

        # Create the ScrollView
        scroll_view = MDScrollView(do_scroll_x=False)

        # Create the parent layout for the cards
        card_layout = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            padding=dp(10),
            spacing=dp(10),
        )

        # Dynamically generate cards for each restaurant
        for restaurant in fetch_restaurants_from_db():
            card = MDCard(
                size_hint_y=None,
                height=dp(200),
                orientation="vertical",
                padding=dp(5),
                spacing=dp(15),
                radius=[dp(10), dp(10), dp(10), dp(10)],
                theme_bg_color="Custom",
                md_bg_color=get_color_from_hex("#492e00de"),
                elevation=dp(10),
                on_release=lambda x, r=restaurant: print(f"Card Clicked: {r[0]}"),
            )

            card.add_widget(
                FitImage(
                    source=restaurant[1],
                    radius=[dp(7.5), dp(7.5), 7.5, 7.5],
                    # size_hint=(0.9, 0.8),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
            )

            # Add content to the card
            card.add_widget(
                MDBoxLayout(
                    orientation="vertical",
                    adaptive_height=True,
                    spacing=dp(25),
                    children=[],
                )
            )

            box_layout = card.children[0]
            box_layout.add_widget(
                MDLabel(
                    text=restaurant[0],
                    halign="center",))
            box_layout.add_widget(
                MDLabel(
                    text=restaurant[2],
                    halign="center",
                    padding=(0, 0, 0, 10),
                ))

            # Add the card to the layout
            card_layout.add_widget(card)

        # Add the layout to the ScrollView
        scroll_view.add_widget(card_layout)

        # Add the ScrollView to the screen
        self.add_widget(scroll_view)
