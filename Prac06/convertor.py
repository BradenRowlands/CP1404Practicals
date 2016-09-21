from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class convertorApp(App):
    def build(self):
        Window.size = (200, 100)
        self.title = "Convertor"
        self.root = Builder.load_file('convertor.kv')
        return self.root

    def convert_to_km(self, distance):
        testBool =  False
        try:
            float(distance) * 1.6402
        except:
            testBool = True
        if testBool == True:
            self.root.ids.display_data.text = str('0.0')
        else:
            total = float(distance) * 1.60934
            self.root.ids.display_data.text = str(total)

    def up_or_down(self, choice, theData):
        try:
            float(theData) + 1
        except:
            theData = float(0)
        if choice == "up":
            total = (float(theData) + 1)
            self.root.ids.get_data.text = str(total)
        elif choice == "down":
            total = (float(theData) - 1)
            self.root.ids.get_data.text = str(total)
        else:
            self.root.ids.get_data.text = str('0.0')
convertorApp().run()