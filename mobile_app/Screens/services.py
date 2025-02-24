from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.divider import MDDivider
from kivymd.uix.label import MDLabel
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

            # Create and store content related to the tab
            content = MDLabel(
                text=f"{tab_name} Content",
                halign="center",
                pos_hint={"center_x": 0.5, "center_y": 0.5}
            )
            self.related_content_container.add_widget(content)

        # Bind the on_tab_switch event to the handler
        self.tabs.bind(on_tab_switch=self.on_tab_switch)

        # Switch to the specified tab
        self.switch_to_selected_tab()

        # Add the layout to the screen
        self.add_widget(layout)

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tabs_label, *args):
        """Update the carousel based on the selected tab."""

        # Retrieve the tab text properly
        tab_text = None
        for child in instance_tab.children:
            if isinstance(child, MDTabsItemText):
                tab_text = child.text
                break

        if not tab_text:
            return  # Safety check to prevent crashes

        if tab_text in self.tab_items:
            tab_index = list(self.tab_items.keys()).index(tab_text)
            self.related_content_container.load_slide(
                self.related_content_container.slides[tab_index]
            )

    def switch_to_selected_tab(self):
        """Switch to the tab that was requested."""
        if self.selected_tab in self.tab_items:
            self.tabs.switch_tab(self.tab_items[self.selected_tab])
            self.on_tab_switch(
                self.tabs,
                self.tab_items[self.selected_tab],
                self.tab_items[self.selected_tab]
            )
        else:
            raise ValueError("Invalid tab name")
