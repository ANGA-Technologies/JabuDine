import sqlite3
import random
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.uix.button import Button
from kivymd.uix.textfield import MDTextField
from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.scrollview import ScrollView

class Account(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db_init()

        # Main layout with ScrollView 
        scroll_view = ScrollView()
        main_layout = MDBoxLayout(
            orientation="vertical", 
            padding="5dp", 
            spacing="10dp", 
            adaptive_height=True,
            size_hint_y=None
        )

        # User Card with dynamic sizing
        user_card = MDCard(
            orientation="vertical",
            size_hint=(0.9, None),  # Responsive width
            height=Window.height * 0.5,  # Proportional height
            pos_hint={"center_x": 0.5},
            elevation=4,
            padding="10dp",
        )

        # User Image
        user_image = Image(
            source="assets/images/profile_placeholder.jpg",
            size_hint=(None, None),
            size=(Window.width * 0.3, Window.width * 0.3), # Responsive size
        )
        user_card.add_widget(user_image)

        # User Details
        details_layout = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            spacing="8dp",
            padding="10dp",
        )

        self.name_field = MDTextField(hint_text="Name", disabled=True)
        self.username_field = MDTextField(hint_text="Username", disabled=True)
        self.email_field = MDTextField(hint_text="Email", disabled=True)
        self.contact_field = MDTextField(hint_text="Contact", disabled=True)

        details_layout.add_widget(self.name_field)
        details_layout.add_widget(self.username_field)
        details_layout.add_widget(self.email_field)
        details_layout.add_widget(self.contact_field)
        user_card.add_widget(details_layout)

        # Buttons with responsive size
        button_layout = MDBoxLayout(
            spacing="10dp", 
            adaptive_height=True, 
            size_hint=(1, None),
        )

        edit_button = Button(
            text="Edit",
            on_release=self.edit_details,
            size_hint=(0.45, None),
            height="50dp",
        )
        save_button = Button(
            text="Save",
            on_release=self.save_details,
            size_hint=(0.45, None),
            height="50dp",
        )

        button_layout.add_widget(edit_button)
        button_layout.add_widget(save_button)
        user_card.add_widget(button_layout)

        # Add card to main layout
        main_layout.add_widget(user_card)
        scroll_view.add_widget(main_layout)
        self.add_widget(scroll_view)

        # Load random user details from the database
        self.load_user_details()

    def db_init(self):
        """Initialize the database and create table if not exists."""
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                username TEXT UNIQUE,
                email TEXT UNIQUE,
                contact TEXT
            )
            """
        )
        conn.commit()
        conn.close()

    def load_user_details(self):
        """Load a random user from the database."""
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users")
        user_ids = cursor.fetchall()

        if user_ids:
            random_id = random.choice(user_ids)[0] # Random user id for testing purposes
            cursor.execute("SELECT name, username, email, contact FROM users WHERE id = ?", (random_id,))
            user = cursor.fetchone()
        else:
            user = None

        conn.close()

        if user:
            self.name_field.text = user[0]
            self.username_field.text = user[1]
            self.email_field.text = user[2]
            self.contact_field.text = user[3]
        else:
            self.name_field.text = "DEFAULT USER"
            self.username_field.text = "DEFAULT_USERNAME"
            self.email_field.text = "DEFAULT"
            self.contact_field.text = "DEFAULT"

    def edit_details(self, *args):
        self.name_field.disabled = False
        self.username_field.disabled = False
        self.email_field.disabled = False
        self.contact_field.disabled = False

    def save_details(self, *args):
        name = self.name_field.text
        username = self.username_field.text
        email = self.email_field.text
        contact = self.contact_field.text

        # Email Validation
        if not email or "@" not in email:
            self.email_field.error = True
            return

        # Contact validation
        if not contact.isdigit() or len(contact) < 10:
            self.contact_field.error = True
            return

        self.name_field.disabled = True
        self.username_field.disabled = True
        self.email_field.disabled = True
        self.contact_field.disabled = True

        # Save to database
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO users (name, username, email, contact)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(username) DO UPDATE SET
                name=excluded.name,
                email=excluded.email,
                contact=excluded.contact
            """,
            (name, username, email, contact),
        )
        conn.commit()
        conn.close()

        print(f"Details Saved:\nName: {name}\nUsername: {username}\nEmail: {email}\nContact: {contact}")
