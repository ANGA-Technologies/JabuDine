from kivy.clock import Clock
from kivymd.app import MDApp
from Screens.home import HomeScreen  # Import from the screens folder

class Main(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Light"
        return HomeScreen()

    def on_start(self):
        def on_start(*args):
            self.root.md_bg_color = self.theme_cls.backgroundColor  # Corrected property for background color

        Clock.schedule_once(on_start)


Main().run()
