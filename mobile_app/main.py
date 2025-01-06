from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_string("""
<HomeScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'JabuDine'
            elevation: 10
        MDRaisedButton:
            text: 'Order Food'
            pos_hint: {'center_x': 0.5}
            on_press: app.switch_to_screen('order')
        MDRaisedButton:
            text: 'Make Reservation'
            pos_hint: {'center_x': 0.5}
            on_press: app.switch_to_screen('reservation')
""")

class HomeScreen(Screen):
    pass

class OrderScreen(Screen):
    pass

class ReservationScreen(Screen):
    pass

class JabuDineApp(MDApp):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(OrderScreen(name='order'))
        self.sm.add_widget(ReservationScreen(name='reservation'))
        return self.sm

    def switch_to_screen(self, screen_name):
        self.sm.current = screen_name

if __name__ == "__main__":
    JabuDineApp().run()








# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# import requests

# class MainScreen(BoxLayout):
#     def fetch_menu(self):
#         response = requests.get('http://127.0.0.1:5454/api/menu-items/')
#         if response.status_code == 200:
#             menu_items = response.json()
#             self.ids.menu_list.text = '\n'.join([item['name'] for item in menu_items])
#         else:
#             self.ids.menu_list.text = "Failed to fetch menu"

# class RestaurantApp(App):
#     def build(self):
#         return MainScreen()

# if __name__ == "__main__":
#     RestaurantApp().run()

