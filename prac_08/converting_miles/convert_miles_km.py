from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

FACTOR_MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    output_km = StringProperty()

    def build(self):
        """App build base on KV file"""
        self.title = 'Convert Miles to Km'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle calculations"""
        print('Calculate')
        miles = self.convert_to_number(text)
        self.root.ids.input_miles.text = str(miles)

    def handle_increments(self, text, change):
        print('Update')
        print("handle increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)
        # Since the InputText.text has changed, its on_text event will fire and handle_calculate will be called

    def update_result(self, miles):
        print("update")
        self.output_km = str(miles * FACTOR_MILES_TO_KM)

    @staticmethod
    def convert_to_number(text):
        try:
            return float(text)
        except ValueError:
            return 0.0
# Missing run function to run the app.
