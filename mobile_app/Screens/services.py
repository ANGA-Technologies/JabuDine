from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.divider import MDDivider
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivymd.uix.tab import (
    MDTabsPrimary,
    MDTabsItem,
    MDTabsItemIcon,
    MDTabsItemText,
    MDTabsCarousel
)

class Services(MDScreen):
    def __init__(self, selected_tab="Reserve", **kwargs):
        super().__init__(**kwargs)
        self.selected_tab = selected_tab  # Store the selected tab

        # Build your screen layout
        layout = FloatLayout()

        # Create and add the tabs widget
        self.tabs = MDTabsPrimary(
            id="tabs",
            pos_hint={"center_x": 0.5, "center_y": 0.95},
        )
        layout.add_widget(self.tabs)

        # Optionally add a divider
        divider = MDDivider(pos_hint={"center_x": 0.5, "center_y": 0.88})
        layout.add_widget(divider)

        # Dictionary to store tab items
        self.tab_items = {}

        # Create the related content container
        self.related_content_container = MDTabsCarousel(
            size_hint_y=None,
            height=dp(320),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        layout.add_widget(self.related_content_container)

        # Add tabs
        for tab_icon, tab_name in {
            "food": "Order",
            "table-chair": "Reserve",
        }.items():
            tab_item = MDTabsItem(
                MDTabsItemIcon(icon=tab_icon),
                MDTabsItemText(text=tab_name),
            )
            self.tabs.add_widget(tab_item)
            self.tab_items[tab_name] = tab_item  # Store tab reference
            content = MDLabel(
                text=f"{tab_name} Content",
                halign="center",
                pos_hint={"center_x": 0.5, "center_y": 0.5}
            )
            self.related_content_container.add_widget(content)

        # Switch to the specified tab
        self.switch_to_selected_tab()

        # Add the layout to the screen
        self.add_widget(layout) 

    def switch_to_selected_tab(self):
        """Switch to the tab that was requested."""
        if self.selected_tab in self.tab_items:
            self.tabs.switch_tab(self.tab_items[self.selected_tab])
            if self.selected_tab == "Order":
                self.related_content_container.load_slide(
                    self.related_content_container.slides[0]
                )
            elif self.selected_tab == "Reserve":
                self.related_content_container.load_slide(
                    self.related_content_container.slides[1]
                )
            else:
                raise ValueError("Invalid tab name")
            