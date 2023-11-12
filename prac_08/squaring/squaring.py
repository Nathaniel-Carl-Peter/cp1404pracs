"""
Cp1404 - Practical
Nathaniel Carl Peter
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):
    """KV app square numbers"""

    def build(self):
        """Build app base from kv file"""
        Window.size = (500, 500)
        self.title = 'Square Numbers'
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculations"""
        try:
            results = int(value) ** 2
            self.root.ids.output_label = str(results)
        except ValueError:
            self.root.ids.output_label.txt = ""


SquareNumberApp().run()
