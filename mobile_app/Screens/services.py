from kivymd.uix.screen import MDScreen
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.divider import MDDivider
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.tab import MDTabsBase
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivymd.uix.tab import (
    MDTabsPrimary,
    MDTabsItem,
    MDTabsItemIcon,
    MDTabsItemText,
)

def get_order_content():
    return Label(
        text="Order Content",
        pos_hint={"center_x": 0.5, "center_y": 0.5}
    )

def get_reserve_content():
    return Label(
        text="Reserve Content",
        pos_hint={"center_x": 0.5, "center_y": 0.5}
    )

class Services(MDScreen):
    def __init__(self, selected_tab="Order", **kwargs):
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

        # a content area to display the tab content
        self.content_area = BoxLayout(
            orientation='vertical',
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            size_hint=(0.8, 0.7)
        )
        layout.add_widget(self.content_area)

        # Dictionary to store tab items
        self.tab_items = {
            "Order": get_order_content,
            "Reserve": get_reserve_content,
        }

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

        # Switch to the specified tab
        self.switch_to_selected_tab()

        # Add the layout to the screen
        self.add_widget(layout) 

    def switch_to_selected_tab(self):
        """Switch to the tab that was requested."""
        if self.selected_tab in self.tab_items:
            self.tabs.switch_tab(self.tab_items[self.selected_tab])

    def on_tab_switch(self, instance_tab: MDTabsBase):
        """Callback for switching tabs."""
        tab_name = instance_tab.text
        self.update_content_area(tab_name)

    def update_content_area(self, tab_name):
        """Update the content area based on the selected tab."""
        self.content_area.clear_widgets()
        if tab_name in self.tab_items:
            content = self.tab_items[tab_name]()
            self.content_area.add_widget(content)
