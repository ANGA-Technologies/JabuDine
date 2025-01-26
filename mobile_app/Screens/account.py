from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFabButton
from kivy.uix.image import Image
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogSupportingText, MDDialogButtonContainer
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDButton, MDButtonText


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
            pos_hint={"center_x": 0.5, "center_y": 0.1},
            elevation=10,
            ripple_behavior=True,
        )

        # Profile Picture
        self.profile_image = Image(
            source="assets/images/profile_placeholder.jpg",
            size_hint=(None, None),
            size=(100, 100),
            pos_hint={"center_x": 0.5},
        )

        # User Info
        user_info_layout = MDBoxLayout(orientation="vertical", spacing=10, padding=10)

        self.username_label = MDLabel(
            text="Username: Developer",
            halign="center",
            font_size="24sp",
        )

        self.email_label = MDLabel(
            text="Email: info@angahub.com",
            halign="center",
            font_size="24sp",
        )

        # Add widgets to user info layout
        user_info_layout.add_widget(self.username_label)
        user_info_layout.add_widget(self.email_label)

        # Add widgets to profile card
        profile_card.add_widget(self.profile_image)
        profile_card.add_widget(user_info_layout)

        # Buttons
        button_layout = MDBoxLayout(
            orientation="vertical",
            spacing=20,
            size_hint=(0.8, None),
            height=120,
            pos_hint={"center_x": 0.5},
        )

        # Edit Profile Button
        edit_profile_button = MDFabButton(
            icon="pencil-outline",
            pos_hint={"center_x": 0.5},
            on_release=self.show_edit_profile_dialog,
        )

        # Logout Button
        logout_button = MDFabButton(
            text="Logout",
            icon="logout",
            pos_hint={"center_x": 0.5},
            theme_text_color="Custom",
            text_color=(1, 0, 0, 1),#red
            on_release=self.logout,
        )

        # Add buttons to layout
        button_layout.add_widget(edit_profile_button)
        button_layout.add_widget(logout_button)

        # Add all widgets to main layout
        main_layout.add_widget(profile_card)
        main_layout.add_widget(button_layout)
        self.add_widget(main_layout)

        self.edit_profile_dialog = None

    def show_edit_profile_dialog(self,instance):
        print("Edit button pressed")
        if not self.edit_profile_dialog:
            # fields for username and email
            self.username_field = MDTextField(
                hint_text="Enter new username", text=self.username_label.text.split(": ")[1]
            )
            self.email_field = MDTextField(
                hint_text="Enter new email", text=self.email_label.text.split(": ")[1]
            )

            # Create a layout for the dialog content
            content = MDBoxLayout(
                orientation="vertical",
                spacing=10,
                padding=20,
                size_hint_y=None,
                height=200,
            )
            content.add_widget(self.username_field)
            content.add_widget(self.email_field)

            # Initialize MDDialog
            self.edit_profile_dialog = MDDialog(
                title="Edit Profile",
                type="custom",
                content_cls=content,
                auto_dismiss=False,
                buttons=[
                    MDDialogButtonContainer(
                        MDButton(
                            MDButtonText(text="Cancel"),
                            style="text",
                            on_release=lambda x: self.close_edit_profile_dialog(),
                        ),
                        MDButton(
                            MDButtonText(text="Save"),
                            style="text",
                            on_release=lambda x: self.save_profile_changes(),
                        ),
                        spacing="8dp",
                    )
                ],
            )
            self.edit_profile_dialog.open()
        self.edit_profile_dialog.open()

    def close_edit_profile_dialog(self):
        if self.edit_profile_dialog:
            self.edit_profile_dialog.dismiss()

    def save_profile_changes(self):
        new_username = self.username_field.text.strip()
        new_email = self.email_field.text.strip()

        if new_username:
            self.username_label.text = f"Username: {new_username}"
        if new_email:
            self.email_label.text = f"Email: {new_email}"

        # Close dialog
        self.close_edit_profile_dialog()

    def logout(self, instance):
        print("Logout button pressed")
