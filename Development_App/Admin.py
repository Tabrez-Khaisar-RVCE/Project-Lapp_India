from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen
import re
from BACKEND_DB import Enter_UD_db
from BACKEND_DB import Retrieve_UD_db
from BACKEND_DB import Drop_UD_db
from BACKEND_DB import Update_Email_ID_UD_db

Builder.load_file('Admin.kv')

class Admin_Users(FloatLayout):
    user_details=[]
    user_name_details=[]
    user_email_details=[]

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def show_user_on_screen(self):
        Headings=[]
        self.user_name_details=[]
        self.user_email_details=[]
        self.user_details=[]

        available_data=Retrieve_UD_db()

        for user_details_in_db in available_data:
            Headings+=[{'text':user_details_in_db[2]},{'text':user_details_in_db[0]},{'text':user_details_in_db[1],'width':dp(200)},{'text':'**********'},{'text':user_details_in_db[3]}]
            self.user_name_details.append(user_details_in_db[0])
            self.user_email_details.append(user_details_in_db[1])
            self.user_details.append(user_details_in_db)

        self.ids.tablular_tool_data.data = Headings

    def clear_details(self):
        self.ids.User_Plant_ID.text=''
        self.ids.User_Access.text=''
        self.ids.User_Email_ID.text=''
        self.ids.User_UserName.text=''

    def add_user_details(self):
        if self.ids.User_UserName.text in self.user_name_details or self.ids.User_Email_ID.text in self.user_email_details: self.ids.err_label.text='User Already Available.'
        elif self.ids.User_UserName.text=='':self.ids.err_label.text='Username is Empty.'
        else:
            if self.ids.User_Plant_ID.text=='': self.ids.err_label.text='Plant ID is empty.'
            elif self.ids.User_Access.text=='': self.ids.err_label.text='User Access is empty.'
            elif self.ids.User_Email_ID.text=='': self.ids.err_label.text='Email ID is empty.'
            elif re.search(r'(@lapp.com)|(@lappindia.com)',self.ids.User_Email_ID.text)==None:
                self.ids.err_label.text='Email ID has to end with a @lapp.com or @lappindia.com'
            else:
                self.ids.err_label.text=''
                Enter_UD_db([self.ids.User_UserName.text,self.ids.User_Email_ID.text,self.ids.User_Plant_ID.text,self.ids.User_Access.text,'Lapp123'])
                self.show_user_on_screen()
                self.clear_details()

    def remove_user_details(self):
        if self.ids.User_Email_ID.text=='root@lapp.com':
            self.ids.err_label.text='Cannot remove root.'
            return
        elif self.ids.User_Email_ID.text in self.user_email_details:
            self.ids.err_label.text=''
            Drop_UD_db(self.ids.User_Email_ID.text)
            self.show_user_on_screen()
            self.clear_details()
        else:
            self.ids.err_label.text='Email ID is not Available'

    def retrieve_user_details(self):
        if self.ids.User_Email_ID.text in self.user_email_details:
            self.ids.err_label.text=''
            self.ids.User_Plant_ID.text=self.user_details[self.user_email_details.index(self.ids.User_Email_ID.text)][2]
            self.ids.User_Access.text=self.user_details[self.user_email_details.index(self.ids.User_Email_ID.text)][3]
            self.ids.User_UserName.text=self.user_details[self.user_email_details.index(self.ids.User_Email_ID.text)][0]
        elif self.ids.User_UserName.text in self.user_name_details:
            self.ids.err_label.text=''
            self.ids.User_Plant_ID.text=self.user_details[self.user_name_details.index(self.ids.User_UserName.text)][2]
            self.ids.User_Access.text=self.user_details[self.user_name_details.index(self.ids.User_UserName.text)][3]
            self.ids.User_Email_ID.text=self.user_details[self.user_name_details.index(self.ids.User_UserName.text)][1]
        else:
            self.ids.err_label.text='User is not Available'

    def modify_user_details(self):
        if self.ids.User_Email_ID.text=='root@lapp.com':
            self.ids.err_label.text='Cannot modify root.'
            return
        if self.ids.User_Email_ID.text in self.user_email_details:
            if self.ids.User_Plant_ID.text=='': self.ids.err_label.text='Plant ID is empty.'
            elif self.ids.User_Access.text=='': self.ids.err_label.text='User Access is empty.'
            elif self.ids.User_UserName.text=='': self.ids.err_label.text='UserName is empty.'
            else:
                self.ids.err_label.text=''
                Update_Email_ID_UD_db([self.ids.User_UserName.text,self.ids.User_Plant_ID.text,self.ids.User_Access.text,self.ids.User_Email_ID.text])
                self.show_user_on_screen()
                self.clear_details()
        else:
            self.ids.err_label.text='Email ID is not Available'

class FixedTextInput(TextInput):
    max_length = 39 # Is one lesser than required amount

    def insert_text(self, substring, from_undo=False):
        if len(self.text) <= self.max_length:
            return super().insert_text(substring, from_undo=from_undo)

class FixedTextInput_10(TextInput):
    max_length = 9 # Is one lesser than required amount

    def insert_text(self, substring, from_undo=False):
        if len(self.text) <= self.max_length:
            return super().insert_text(substring, from_undo=from_undo)

class EmailTextInput(TextInput):
    max_length = 99 # Is one lesser than required amount

    def insert_text(self, substring, from_undo=False):
        if len(self.text) <= self.max_length:
            return super().insert_text(substring, from_undo=from_undo)

# class Machine_tool(App):
#     Run_file = ObjectProperty(None)
#
#     def build(self):
#         self.Run_file = Admin_Users()
#         return self.Run_file
#
# Machine_tool().run()
