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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Build your screen layout
        layout = FloatLayout()

        # Create and add the tabs widget
        self.tabs = MDTabsPrimary(
            id="tabs",
            pos_hint={"center_x": 0.5, "center_y": 0.95},
        )
        layout.add_widget(self.tabs)
        
        # Optionally add a divider
        layout.add_widget(MDDivider())
        
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
            
        # Switch to the "Order" tab after all tabs are added
        self.tabs.switch_tab(text="Order")

        # Add the layout to the screen
        self.add_widget(layout)
