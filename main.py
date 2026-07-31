from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

KV = '''
ScreenManager:
    HomeScreen:

<HomeScreen>:
    name: "home"

    BoxLayout:
        orientation: "vertical"
        padding: "20dp"
        spacing: "20dp"

        Label:
            text: "SmartAI"
            font_size: "32sp"
            bold: True

        Label:
            text: "Welcome to SmartAI"
            font_size: "20sp"

        Button:
            text: "Start"
            size_hint_y: None
            height: "50dp"
            on_release:
                app.start_ai()
'''

class HomeScreen(Screen):
    pass


class SmartAI(App):

    def build(self):
        self.title = "SmartAI"
        return Builder.load_string(KV)

    def start_ai(self):
        print("SmartAI Started")


if __name__ == "__main__":
    SmartAI().run()
