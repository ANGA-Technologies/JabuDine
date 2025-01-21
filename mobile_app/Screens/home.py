from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Line
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon, MDFabButton
from Screens.account import Account 
from kivymd.uix.swiper import MDSwiper, MDSwiperItem
from kivy.uix.widget import Widget
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.fitimage import FitImage
from kivy.utils import get_color_from_hex

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

        explore_swipper = MDSwiper(
            size_hint=(1, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.25},
            # background_color=get_color_from_hex("#fff7ea"),
        )

        explore_swipper.add_widget(
            MDSwiperItem(
                # fitimage="assets/images/food1.jpg",
               
                radius= 10,
                size_hint=(0.99, 0.9),
                theme_bg_color="Custom",
                md_bg_color=get_color_from_hex("#000000"),
            )
        )
        explore_swipper.add_widget(
            MDSwiperItem(
                radius= 10,
                size_hint=(0.99, 0.9),
                md_bg_color=get_color_from_hex("#0d3c5c"),
                # text="Menu",
                # icon="silverware-variant",
            )
        )

        layout.add_widget(explore_swipper)

        # Add the main layout to the screen
        self.add_widget(layout)

        self.dropdown_menu = None

    def open_account_page(self):
        """Callback to open the Account page."""
        self.manager.current = "Account"
        
        # Dismiss the dropdown menu when navigating
        if self.dropdown_menu:
            self.dropdown_menu.dismiss()

    def menu(self, button):
        menu_items = [
            {
                "text": "Account",
                "leading_icon": "account-circle",
                "on_release": lambda: self.open_account_page(),
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