from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.core.window import Window
from Navigation_screen_manager import NavigationScreenManager
from kivy.properties import ObjectProperty
# Window.size=(dp(1220),dp(780))

class The_screen_2(NavigationScreenManager):
    pass

class the_lab(App):
    manager = ObjectProperty(None)
    def build(self):
        self.manager=The_screen_2()
        return self.manager

the_lab().run()
