from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.divider import MDDivider
from kivymd.uix.tab import (
    MDTabsPrimary,
    MDTabsItem,
    MDTabsItemIcon,
    MDTabsItemText,
    MDTabsBadge,
)

class Services(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
        layout = FloatLayout()

        layout.add_widget(
            MDTabsPrimary(
                id="tabs",
                pos_hint={"center_x": .5, "center_y": .95},
            ),
            MDDivider(),
        )


        for tab_icon, tab_name in {
            "food": "Order",
            "table-chair": "Reserve",
        }.items():
            if tab_icon == "food":
                self.root.tabs.add_widget(
                    MDTabsItem(
                        MDTabsItemIcon(
                            icon=tab_icon,
                        ),
                        MDTabsItemText(
                            text=tab_name,
                        ),
                    )
                )
            else:
                self.root.tabs.add_widget(
                    MDTabsItem(
                        MDTabsItemIcon(
                            icon=tab_icon,
                        ),
                        MDTabsItemText(
                            text=tab_name,
                        ),
                    )
                )
            self.root.tabs.switch_tab(text="Order")

Services().run()