from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Line
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon, MDFabButton
from Screens.account import Account 
from kivymd.uix.swiper import MDSwiper, MDSwiperItem
from kivy.uix.widget import Widget
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.fitimage import FitImage
from kivy.utils import get_color_from_hex

import sqlite3
import random

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Float Layout for flexibility
        layout = FloatLayout()
        
        menu_button = MDButton(
            MDButtonIcon(
                icon="dots-horizontal",
                color=get_color_from_hex("#ffffff"),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            ),
            style="text",
            size_hint=(None, None),
            size=(dp(15), dp(15)),
            pos_hint={"center_x": 0.9, "center_y": 0.8},
        )
        menu_button.bind(on_release=lambda instance: self.menu(menu_button))
        
        layout.add_widget(menu_button)

        # Greeting Label
        layout.add_widget(
            MDLabel(
                adaptive_size=True,
                text="Hello, Foodie!",
                role="large",
                font_style="Title",
                halign="center",
                pos_hint={"center_x": 0.3, "center_y": 0.8},
            )
        )

        # Logo/Title Label
        layout.add_widget(
            MDLabel(
                text="JabuDine",
                theme_font_name="Custom",
                font_name="assets/fonts/fanfarron.otf",
                font_style="Display",
                halign="center",
                theme_text_color="Custom",
                text_color=get_color_from_hex("#492e00"),
                pos_hint={"center_x": 0.5, "center_y": 0.87},
            )
        )

        # Subtitle Label
        layout.add_widget(
            MDLabel(
                text="Your Table, Your Taste!",
                theme_font_name="Custom",
                font_name="assets/fonts/creame.ttf",
                theme_text_color="Custom",
                font_style="Headline",
                role="medium",
                halign="center",
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
            pos_hint={"center_x": 0.5, "center_y": 0.55},
        )

        # Spacer Widget to center buttons
        buttons_layout.add_widget(Widget(size_hint_x=1))  # Left spacer

        # Order Button
        order_button = MDButton(
            MDButtonText(
                text="Order",
                theme_text_color="Custom",
                text_color=get_color_from_hex("#492e00"),
            ),
            theme_bg_color="Custom",
            theme_shadow_color="Custom",
            shadow_color=get_color_from_hex("#492e00"),
            md_bg_color=get_color_from_hex("#ffffff"),
            style="elevated",
        )

        # Reserve Button
        reserve_button = MDButton(
            MDButtonText(
                text="Reserve",
                theme_text_color="Custom",
                text_color=get_color_from_hex("#492e00"),
            ),
            theme_bg_color="Custom",
            theme_shadow_color="Custom",
            shadow_color=get_color_from_hex("#492e00"),
            md_bg_color=get_color_from_hex("#ffffff"),
            style="elevated",
        )

        # Add buttons to the layout
        buttons_layout.add_widget(order_button)
        buttons_layout.add_widget(reserve_button)

        # Spacer Widget to center buttons
        buttons_layout.add_widget(Widget(size_hint_x=1))  # Right spacer

        # Add the buttons layout to the main layout
        layout.add_widget(buttons_layout)

        # Function to fetch top rated restaurants from the database
        def fetch_restaurants_from_db():
            db_path = "assets\db\jabudine.db"  # Replace with the path to your .db file
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Fetch restaurants with rating of 5
            cursor.execute("SELECT name, img, location FROM restaurants WHERE rating = 5")
            restaurants = cursor.fetchall()

            conn.close()

            # Randomly pick up to 10 restaurants
            return random.sample(restaurants, min(5, len(restaurants))) if restaurants else []
        
        # Creating the explore_swipper and populating it dynamically
        explore_swipper = MDSwiper(
            size_hint=(1, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.25},
        )

        # Fetch the data
        restaurants = fetch_restaurants_from_db()

        # Add widgets dynamically for each restaurant
        for restaurant in restaurants:
            name, image_path, location = restaurant

            swiper_item = MDSwiperItem(
                FitImage(
                    source=image_path,  # Restaurant image
                    radius=7.5,
                    size_hint=(1, 0.7),
                ),
                MDLabel(
                    text=name,
                    font_name="Times",
                    theme_text_color="Custom",
                    text_color=get_color_from_hex("#ffffff"),
                    size_hint=(1, 0.1),
                    padding=(10, 0),
                ),

                # Proper addition of MDBoxLayout with widgets inside
                MDBoxLayout(
                    # halign="center",
                    orientation="horizontal",
                    size_hint=(1, 0.1),
                    spacing=10,  # Add spacing for visibility
                    padding=(10, 0),  # Padding to avoid overlap
                    pos_hint={"center_x": 0.5, "center_y": 0.5},  # Positioning
                    children=[]
                ),
                orientation="vertical",
                padding=5,
                radius=10,
                size_hint=(0.99, 0.9),
                theme_bg_color="Custom",
                md_bg_color=get_color_from_hex("#492e00"),
            )

            # Create the icon and label and add them to the box layout
            box_layout = swiper_item.children[0]  # Get the MDBoxLayout
            box_layout.add_widget(MDIcon(
                icon="map-marker",
                theme_text_color="Custom",
                text_color=get_color_from_hex("#d8d8d8"),
                size_hint=(None, None),
                # x = dp(5),
            ))
            box_layout.add_widget(MDLabel(
                text=location, 
                theme_text_color="Custom",
                text_color=get_color_from_hex("#d8d8d8"),
                halign="left"
            ))

            explore_swipper.add_widget(swiper_item)

        swiper_item = MDSwiperItem(
            MDButton(
                MDButtonText(
                    text="More",
                    theme_text_color="Custom",
                    text_color=get_color_from_hex("#ffffff"),
                ),
                size_hint=(None, None),
                pos_hint={"center_x": 0.2, "center_y": 0.5},
                theme_bg_color="Custom",
                theme_shadow_color="Custom",
                shadow_color=get_color_from_hex("#ffffff"),
                md_bg_color=get_color_from_hex("#492e00"),
                style="elevated",
                on_release = self.open_explore_page
            ),
            orientation="vertical",
            padding=5,
            size_hint=(0.3, 0.3),
        )

        explore_swipper.add_widget(swiper_item)

        layout.add_widget(explore_swipper)

        # Add the main layout to the screen
        self.add_widget(layout)

        self.dropdown_menu = None

    def open_explore_page(self, *args):
        app = MDApp.get_running_app()
        app.switch_to_screen("Explore")


    def open_account_page(self):
        """Callback to open the Account page."""
        # self.manager.current = "Account"
        app = MDApp.get_running_app()
        app.switch_to_screen("Account")
        
        # Dismiss the dropdown menu when navigating
        if self.dropdown_menu:
            self.dropdown_menu.dismiss()

    def menu(self, button):
        menu_items = [
            {
                "text": "Account",
                "leading_icon": "account-circle",
                "on_release": self.open_account_page,
            },
            {
                "text": "Settings",
                "leading_icon": "cog",
            },
            {
                "text": "Logout",
                "leading_icon": "logout",
            }
        ]
        
        # Create and store the dropdown menu
        self.dropdown_menu = MDDropdownMenu(
            caller=button,
            items=menu_items,
        )
        
        # Open the dropdown menu
        self.dropdown_menu.open()