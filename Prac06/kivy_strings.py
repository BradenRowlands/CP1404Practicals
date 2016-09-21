
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

class kivyStringsApp(App):
    stringList = ["hello","bonjour","g'day"]

    def build(self):
        self.title = "Kivy Strings"
        self.root = Builder.load_file('kivy_strings.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.stringList:
            temp_button = Button(text=name)
            self.root.ids.entriesBox.add_widget(temp_button)

kivyStringsApp().run()