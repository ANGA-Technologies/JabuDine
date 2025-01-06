from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDButton, MDButtonText


class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Light" 
        return MDScreen(
            MDButton(
                MDButtonText(
                    text="Jab to Dine",
                ),
                style="outlined",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )

    def on_start(self):
        def on_start(*args):
            self.root.md_bg_color = self.theme_cls.backgroundColor

        Clock.schedule_once(on_start)


Example().run()