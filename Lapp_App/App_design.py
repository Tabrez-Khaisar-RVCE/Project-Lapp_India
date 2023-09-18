from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp


Builder.load_file('App_design.kv')

# class StackLayoutExample(StackLayout):
#     def __init__(self,**kwargs):
#         super().__init__(**kwargs)
#         for i in range(1,101):
#             b=Button(text=str(i),size_hint=(None,None),size=(dp(100),dp(100)))
#             self.add_widget(b)
