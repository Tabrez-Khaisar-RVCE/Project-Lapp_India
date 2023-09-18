from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen
import re


class REP_MOD_Machine_Tool(BoxLayout):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def on_screen_display(self,Component,Description,corecolor):
        data_holder=[]
        for cores in [['pizza','noodles','taco','burger','maggi','manchurian','icecream']]:
            data_holder+=[{'text':cores[0],'width':dp(150)},{'text':cores[1],'width':dp(200)},{'text':cores[2]},{'text':cores[3]},{'text':cores[4]},{'text':cores[5]},{'text':cores[6]}]

        self.ids.tablular_data_cores.data=data_holder
        print(self.ids.tablular_data_cores.data)
        print(data_holder)

    def clear_screen(self):
        self.ids.Operation_Type.text=''
        self.ids.Machine_Type.text=''
        self.ids.Machine_Tool_ID.text=''
        self.ids.Plant_ID_8235.text=''
        self.ids.Plant_ID_8261.text=''
        self.ids.Plant_ID_8233.text=''
        self.ids.Plant_ID_8273.text=''

    def Details(self):
        self.ids.err_label.text=''
        if self.ids.Operation_Type.text=='':
            self.ids.err_label.text='Operation Type is Empty.'
            return
        if self.ids.Machine_Type.text=='':
            self.ids.err_label.text='Machine Type is Empty.'
            return
        if self.ids.Machine_Tool_ID.text=='':
            self.ids.err_label.text='Machine Tool ID is Empty.'
            return

        if self.ids.Plant_ID_8235.text=='':self.ids.Plant_ID_8235.text='NA'
        if self.ids.Plant_ID_8261.text=='':self.ids.Plant_ID_8261.text='NA'
        if self.ids.Plant_ID_8233.text=='':self.ids.Plant_ID_8233.text='NA'
        if self.ids.Plant_ID_8273.text=='':self.ids.Plant_ID_8273.text='NA'

        return [self.ids.Operation_Type.text,self.ids.Machine_Type.text,self.ids.Machine_Tool_ID.text,self.ids.Plant_ID_8235.text,self.ids.Plant_ID_8261.text,self.ids.Plant_ID_8233.text,self.ids.Plant_ID_8273.text]

    def Add_details(self):
        new_details_holder=[]

        if new_details_holder==[]: # the_details_db()
            Add_tool_details=self.details
            if not Add_tool_details==None:
                #add_Details_db(Add_tool_details)
            self.clear_screen()
            print('pizza')
        else:
            self.ids.err_label.text='Machine Tool ID is Already Available.'


    def Remove_details(self):
        new_details_holder=[]
        if not new_details_holder==[]: # the_details_db()
            # remove_details_db()
            self.clear_screen()
        else:
            self.ids.err_label.text='Machine Tool ID is Not Available.'

    def Retrieve_details(self):
        new_details_holder=[]
        if not new_details_holder==[]: # the_details_db()
            self.ids.Operation_Type.text=new_details_holder[]
            self.ids.Machine_Type.text=new_details_holder[]
            self.ids.Machine_Tool_ID.text=new_details_holder[]
            self.ids.Plant_ID_8235.text=new_details_holder[]
            self.ids.Plant_ID_8261.text=new_details_holder[]
            self.ids.Plant_ID_8233.text=new_details_holder[]
            self.ids.Plant_ID_8273.text=new_details_holder[]
        else:
            self.ids.err_label.text='Machine Tool ID is Not Available.'

    def Modify_details(self):
        if not new_details_holder==[]:# the_details_db()
            Modify_tool_details=self.details
            if not Modify_tool_details==None:
                #Modify_Details_db(Add_tool_details)
            self.clear_screen()
        else:
            self.ids.err_label.text='Machine Tool ID is Not Available.'

class FixedTextInput(TextInput):
    max_length = 39 # Is one lesser than required amount

    def insert_text(self, substring, from_undo=False):
        if len(self.text) <= self.max_length:
            return super().insert_text(substring, from_undo=from_undo)

class PositiveTextInput(FixedTextInput):
    def insert_text(self, substring, from_undo=False):

        if self.text=='-':
            self.text=''
        else:
            return super().insert_text(substring, from_undo=from_undo)

class Machine_tool(App):
    Run_file = ObjectProperty(None)

    def build(self):
        self.Run_file = REP_MOD_Machine_Tool()
        return self.Run_file

Machine_tool().run()
