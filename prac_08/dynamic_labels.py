from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

NEW_COLOUR = (1, 0, 0, 1)
ALTERNATIVE_COLOUR = (1, 0, 1, 1)


class DynamicWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.name_to_phone:
            temp_button = Button(text=name)
            temp_button.bind(on_press=self.press_entry)
            temp_button.background_color = NEW_COLOUR
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.text
        instance.background_color = ALTERNATIVE_COLOUR
        self.status_text = f"{name}'s number is {self.name_to_phone[name]}"

    def clear_all(self):
        self.root.ids.entries_box.clear_widgets()


DynamicWidgetsApp().run()