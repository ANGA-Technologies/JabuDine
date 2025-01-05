from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import requests

class MainScreen(BoxLayout):
    def fetch_menu(self):
        response = requests.get('http://127.0.0.1:5454/api/menu-items/')
        if response.status_code == 200:
            menu_items = response.json()
            self.ids.menu_list.text = '\n'.join([item['name'] for item in menu_items])
        else:
            self.ids.menu_list.text = "Failed to fetch menu"

class RestaurantApp(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    RestaurantApp().run()
