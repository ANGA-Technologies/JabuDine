from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.app import MDApp
from Screens.home import HomeScreen  # Import from the screens folder
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Rectangle

# Set the window size directly
Window.size = (360, 640)  # Width and height in pixels

class GradientWidget(HomeScreen):
    def __init__(self, start_color=(1, 1, 1, 1), end_color=(1, 0, 0, 1), steps=50, **kwargs):
        super().__init__(**kwargs)
        self.start_color = start_color
        self.end_color = end_color
        self.steps = steps

        with self.canvas.before:
            self.rects = []  # We'll store references to each rectangle
            for i in range(steps):
                # Each rectangle will get its own Color + Rectangle
                color = self._interpolate_color(start_color, end_color, i / (steps - 1))
                Color(*color)
                rect = Rectangle(pos=self.pos, size=(self.width, self.height / steps))
                self.rects.append(rect)

        # We need to update rectangles whenever pos/size changes
        self.bind(pos=self._update_rects, size=self._update_rects)

    def _update_rects(self, *args):
        strip_height = self.height / float(self.steps)
        for i, rect in enumerate(self.rects):
            rect.pos = (self.x, self.y + i * strip_height)
            rect.size = (self.width, strip_height)

    def _interpolate_color(self, c1, c2, t):
        # Linear interpolation of RGBA
        return (
            c1[0] + (c2[0] - c1[0]) * t,
            c1[1] + (c2[1] - c1[1]) * t,
            c1[2] + (c2[2] - c1[2]) * t,
            c1[3] + (c2[3] - c1[3]) * t
        )

class Main(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"

        # from white (top) to orange (bottom):
        return GradientWidget(start_color=get_color_from_hex("#E59400"), end_color=get_color_from_hex("#FFFFFF"), steps=64)

Main().run()
