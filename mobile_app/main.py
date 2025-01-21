from kivy.core.window import Window
from Screens.home import HomeScreen  # Import from the screens folder
from Screens.alerts import Alerts  # Import from the screens folder
from Screens.explore import Explore  # Import from the screens folder
from Screens.menu import Menu  # Import from the screens folder
from Screens.account import Account  # Import from the screens folder
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
# from kivy.uix.screenmanager import FadeTransition
from kivymd.uix.transition import MDSwapTransition, MDSharedAxisTransition, MDFadeSlideTransition
from kivymd.uix.navigationbar import (
    MDNavigationBar,
    MDNavigationItem,
    MDNavigationItemLabel,
    MDNavigationItemIcon,
)

# Set the window size
Window.size = (320, 540)


class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_widget(MDNavigationItemIcon(icon=self.icon))
        self.add_widget(MDNavigationItemLabel(text=self.text))


class JabuDine(MDApp):
    def on_switch_tabs(
        self,
        bar: MDNavigationBar,
        item: MDNavigationItem,
        item_icon: str,
        item_text: str,
    ):
        # Switch the screen in the ScreenManager based on the selected navigation item
        self.root.get_ids().screen_manager.current = item_text

    def build(self):
        return MDBoxLayout(
            MDScreenManager(
                HomeScreen(
                    name="Home",  # Use the imported HomeScreen
                ),
                Menu(
                    name="Menu",  # Use the imported Menu screen
                ),
                Alerts(
                    name="Alerts",  # Use the imported Alerts screen
                ),
                Explore(
                    name="Explore",  # Use the imported Explore screen
                ),
                Account(
                    name="Account",  # Use the imported Account screen
                    transition_progress = 12, 
                    transition_state = 'out',
                ),
                transition=MDSwapTransition(),
                # transition_axis = 'y',
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
                md_bg_color=get_color_from_hex("#fff7ea"),
                on_switch_tabs=self.on_switch_tabs,
            ),
            
            orientation="vertical",
            md_bg_color=get_color_from_hex("#ffffff"),
        )

if __name__ == "__main__":
    JabuDine().run()