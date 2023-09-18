from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.stacklayout import StackLayout
# from kivy.uix.scrollview import ScrollView
# from kivy.metrics import dp
# from kivy.core.window import Window
from Push_Pop_screens import Push_Pop_screens
from kivy.properties import ObjectProperty
# Window.size=(dp(1220),dp(780))

class Screen_Manager(Push_Pop_screens):
    pass

class LAPP_OLFLEX_Connect(App):
    Run_file = ObjectProperty(None)
    def build(self):
        self.icon = 'Design_considerations/Images/App_Icon.png'
        self.Run_file=Screen_Manager()
        return self.Run_file

LAPP_OLFLEX_Connect().run()
