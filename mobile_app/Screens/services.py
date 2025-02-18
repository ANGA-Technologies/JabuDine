from kivymd.uix.screen import MDScreen
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.divider import MDDivider
from kivymd.uix.tab import (
    MDTabsPrimary,
    MDTabsItem,
    MDTabsItemIcon,
    MDTabsItemText,
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
        
        # add a divider
        divider = MDDivider(pos_hint={"center_x": 0.5, "center_y": 0.88})
        layout.add_widget(divider)
        
        # Dictionary to store tab items
        self.tab_items = {}

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
            self.tabs.switch_tab(self.selected_tab)