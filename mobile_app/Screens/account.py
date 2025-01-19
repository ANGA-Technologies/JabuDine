#from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDButton, MDButtonText
from kivy.uix.image import Image


class Account(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Main layout
        main_layout = MDBoxLayout(orientation="vertical", padding=20, spacing=20)

        # Profile Card
        profile_card = MDCard(
            orientation="vertical",
            padding=20,
            size_hint=(0.9, 0.4),
            # pos_hint={"center_x": 0.5},
            pos_hint={"center_x": 0.5, "center_y": 0.1},
            elevation=10,
            ripple_behavior=True,
        )

        # Profile Picture
        profile_image = Image(
            source="assets/images/profile_placeholder.jpg",
            size_hint=(None, None),
            size=(100, 100),
            pos_hint={"center_x": 0.5},
        )

        # User Info
        user_info_layout = MDBoxLayout(orientation="vertical", spacing=10, padding=10)

        username_label = MDLabel(
            text="Username: Developer",
            halign="center",
            font_size="18sp",
        )

        email_label = MDLabel(
            text="Email: info@angahub.com",
            halign="center",
            font_size="18sp",
        )

        # Add widgets to user info layout
        user_info_layout.add_widget(username_label)
        user_info_layout.add_widget(email_label)

        # Add widgets to profile card
        profile_card.add_widget(profile_image)
        profile_card.add_widget(user_info_layout)

        # Buttons
        button_layout = MDBoxLayout(
            orientation="vertical", spacing=10, size_hint=(0.8, None), pos_hint={"center_x": 0.5}
        )

        # Edit Profile Button
        edit_profile_button = MDButton(
            MDButtonText(text="Edit Profile"),
            pos_hint={"center_x": 0.5},
            size_hint=(None, None),
            size=(150, 50),
            on_release=self.edit_profile,
        )

        # Logout Button
        logout_button = MDButton(
            MDButtonText(text="Logout"),
            pos_hint={"center_x": 0.5},
            size_hint=(None, None),
            size=(150, 50),
            on_release=self.logout,
        )

        # Add buttons to layout
        button_layout.add_widget(edit_profile_button)
        button_layout.add_widget(logout_button)

        # Add all widgets to main layout
        main_layout.add_widget(profile_card)
        main_layout.add_widget(button_layout)
        self.add_widget(main_layout)

    def edit_profile(self, instance):
        # Functionality for editing profile to be added
        print("Edit Profile button pressed")

    def logout(self, instance):
        # Functionality for logging out to be added
        print("Logout button pressed")
