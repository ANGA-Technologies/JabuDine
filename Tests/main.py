from kivy.core.window import Window
# from Screens.home import HomeScreen  # Import from the screens folder
# from Screens.alerts import Alerts  # Import from the screens folder
# from Screens.explore import Explore  # Import from the screens folder
# from Screens.menu import Menu  # Import from the screens folder
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.fitimage import FitImage
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationbar import (
    MDNavigationBar,
    MDNavigationItem,
    MDNavigationItemLabel,
    MDNavigationItemIcon,
)


# Set the window size
Window.size = (320, 640)


class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_widget(MDNavigationItemIcon(icon=self.icon))
        self.add_widget(MDNavigationItemLabel(text=self.text))


class BaseScreen(MDScreen):
    image_size = StringProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        with self.canvas.before:
            # Set the light orange background color
            # Color(*get_color_from_hex("#FFE5B4"))
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self._update_rect, size=self._update_rect)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

        self.add_widget(
            FitImage(
                source=f"https://picsum.photos/{self.image_size}/{self.image_size}",
                size_hint=(0.9, 0.9),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                radius=dp(24),
            ),
        )


class Main(MDApp):
    def on_switch_tabs(
        self,
        bar: MDNavigationBar,
        item: MDNavigationItem,
        item_icon: str,
        item_text: str,
    ):
        self.root.get_ids().screen_manager.current = item_text

    def build(self):
        return MDBoxLayout(
            MDScreenManager(
                BaseScreen(
                    name="Home",
                    image_size="1024",
                ),
                BaseScreen(
                    name="Menu",
                    image_size="800",
                ),
                BaseScreen(
                    name="Alerts",
                    image_size="600",
                ),
                BaseScreen(
                    name="Explore",
                    image_size="700",
                ),
                id="screen_manager",
            ),
            MDNavigationBar(
                BaseMDNavigationItem(
                    icon="home",
                    text="Home",
                    active=True,
                    ripple_color=get_color_from_hex("#55452a"),
                ),
                BaseMDNavigationItem(
                    icon="silverware-variant",
                    text="Menu",
                    ripple_color=get_color_from_hex("#55452a")
                ),
                BaseMDNavigationItem(
                    icon="bell",
                    text="Alerts",
                    ripple_color=get_color_from_hex("#55452a")
                ),
                BaseMDNavigationItem(
                    icon="bookmark-multiple",
                    text="Explore",
                    ripple_color=get_color_from_hex("#55452a")
                ),
                theme_bg_color="Custom",
                md_bg_color=get_color_from_hex("#ffd58d"),
                on_switch_tabs=self.on_switch_tabs,
            ),
            orientation="vertical",
            md_bg_color=get_color_from_hex("#ffeccc"),
        )


Main().run()
