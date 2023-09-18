from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty

Builder.load_file('Boxlayout_with_action_bar.kv')

class Boxlayoutwithactionbar(BoxLayout):
    title=StringProperty()
