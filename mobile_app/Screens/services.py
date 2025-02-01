from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.tab import (
    MDTabsItem,
    MDTabsItemIcon,
    MDTabsItemText,
    MDTabsBadge,
)

KV = '''
FloatLayout:
    # md_bg_color: self.theme_cls.backgroundColor

    MDTabsPrimary:
        id: tabs
        pos_hint: {"center_x": .5, "center_y": .95}

        MDDivider:
'''


class Services(MDApp):
    def on_start(self):
        for tab_icon, tab_name in {
            "food": "Order",
            "table-chair": "Reserve",
        }.items():
            if tab_icon == "cart":
                self.root.ids.tabs.add_widget(
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
                self.root.ids.tabs.add_widget(
                    MDTabsItem(
                        MDTabsItemIcon(
                            icon=tab_icon,
                        ),
                        MDTabsItemText(
                            text=tab_name,
                        ),
                    )
                )
            self.root.ids.tabs.switch_tab(text="Trips")

    def build(self):
        # self.theme_cls.primary_palette = "Red"
        return Builder.load_string(KV)


Services().run()