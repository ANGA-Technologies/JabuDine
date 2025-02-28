from kivy.core.window import Window
from Screens.home import HomeScreen  # Import from the screens folder
from Screens.alerts import Alerts  # Import from the screens folder
from Screens.explore import Explore  # Import from the screens folder
from Screens.menu import Menu  # Import from the screens folder
from Screens.account import Account  # Import from the screens folder
from Screens.services import Services # Import from the screens folder

from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
# from kivy.uix.screenmanager import FadeTransition
from kivymd.uix.transition import MDSwapTransition, MDSharedAxisTransition, MDFadeSlideTransition, MDSlideTransition
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

    def switch_to_screen(self, screen_name: str):
        # Switch the screen in the ScreenManager
        screen_manager = self.root.get_ids().screen_manager
        screen_manager.current = screen_name

        # Update the active state of the navigation bar
        navigation_bar = self.root.children[0]  # Assuming navigation bar is the first child
        for nav_item in navigation_bar.children:
            nav_item.active = nav_item.text == screen_name

    def build(self):
        return MDBoxLayout(
            MDScreenManager(
                HomeScreen(
                    name="Home",  # Use the imported HomeScreen
                ),
                Menu(
                    name="Dishes",  # Use the imported Menu screen
                ),
                Alerts(
                    name="Alerts",  # Use the imported Alerts screen
                ),
                Explore(
                    name="Explore",
                ),
                Account(
                    name="Account",  # Use the imported Account screen
                    transition_progress = 12, 
                    transition_state = 'out',
                ),
                Services(
                    name="Services",  # Use the imported Services screen
                ),
                # transition=MDSwapTransition(),
                transition=MDSlideTransition(duration=0.3, direction="left"),
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
                    text="Dishes", 
                    ripple_color=get_color_from_hex("#55452a")
                ),
                BaseMDNavigationItem(
                    icon="bookmark-multiple",
                    text="Explore",
                    ripple_color=get_color_from_hex("#55452a")
                ),
                BaseMDNavigationItem(
                    icon="bell",
                    text="Alerts",
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

