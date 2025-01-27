from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.uix.button import Button
from kivymd.uix.textfield import MDTextField
from kivy.uix.image import Image
# from kivymd.toast import toast

class Account(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Main layout
        main_layout = MDBoxLayout(orientation="vertical", padding=20, spacing=20)

        # User Card
        user_card = MDCard(
            orientation="vertical",
            size_hint=(None, None),
            size=(300, 450),
            pos_hint={"center_x": 0.5},
            elevation=4,
            padding=20,
        )

        # User Image
        user_image = Image(
            source="assets/images/profile_placeholder.jpg",
            size_hint_y=None,
            height=120,
        )
        user_card.add_widget(user_image)

        # User Details
        details_layout = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            spacing=12,
            padding=10,
        )

        self.name_field = MDTextField(
            hint_text="Name",
            text="Developer",
            disabled=True
        )
        self.username_field = MDTextField(
            hint_text="Username",
            text="EA_Miles",
            disabled=True
        )
        self.email_field = MDTextField(
            hint_text="Email",
            text="Developer@angahub.com",
            disabled=True
        )
        self.contact_field = MDTextField(
            hint_text="Contact",
            text="0123456789",
            disabled=True,
            # helper_text="Enter a valid phone number",
            # helper_text_mode="on_error"
        )

        details_layout.add_widget(self.name_field)
        details_layout.add_widget(self.username_field)
        details_layout.add_widget(self.email_field)
        details_layout.add_widget(self.contact_field)
        user_card.add_widget(details_layout)

        # Buttons
        button_layout = MDBoxLayout(spacing=10, adaptive_height=True)

        edit_button = Button(
            text="Edit",
            #icon="pencil-outline",
            on_release=self.edit_details,
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={"center_x": 0.5}
        )
        save_button = Button(
            text="Save",
            on_release=self.save_details,
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={"center_x": 0.5}
        )

        button_layout.add_widget(edit_button)
        button_layout.add_widget(save_button)
        user_card.add_widget(button_layout)

        # Add card to main layout
        main_layout.add_widget(user_card)
        self.add_widget(main_layout)

    def edit_details(self, *args):
        self.name_field.disabled = False
        self.username_field.disabled = False
        self.email_field.disabled = False
        self.contact_field.disabled = False
        # toast("Editing details...")

    #Save new user details
    def save_details(self, *args):
        name = self.name_field.text
        username = self.username_field.text
        email = self.email_field.text
        contact = self.contact_field.text

        # Email Validation
        if not email or "@" not in email:
            self.email_field.error = True
            # toast("Invalid email address")
            return

        #Contact validation
        if not contact.isdigit() or len(contact) < 10:
            self.contact_field.error = True
            # toast("Invalid contact number")
            return

        self.name_field.disabled = True
        self.username_field.disabled = True
        self.email_field.disabled = True
        self.contact_field.disabled = True

        # toast("Details saved successfully")
        print(f"Details Saved:\nName: {name}\nUsername: {username}\nEmail: {email}\nContact: {contact}")
