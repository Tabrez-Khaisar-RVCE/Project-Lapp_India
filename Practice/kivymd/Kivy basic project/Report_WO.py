from kivy.app import App
from kivy.lang import Builder
# from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from Push_Pop_screens import Push_Pop_screens
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import os

class Retrieve_xlsx_file(BoxLayout):
    confirm = ObjectProperty(None)
    cancel = ObjectProperty(None)
    file_location = ObjectProperty(None)

class WO_filechooser(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_Retrieve_xlsx_file(self):
        content = Retrieve_xlsx_file(confirm=self.take_file_location,cancel=self.dismiss_popup)
        self._popup = Popup(title="WO File location", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def take_file_location(self, file_path):
        if file_path=='':
            self.ids.file_location_main.text='Choose WO Location.'
        else:
            self.ids.file_location_main.text=file_path
        self.dismiss_popup()




class test(App):
    Run_file = ObjectProperty(None)

    def build(self):
        self.icon = 'Design_considerations/Images/App_Icon.png'
        self.Run_file = WO_filechooser()
        return self.Run_file

test().run()
