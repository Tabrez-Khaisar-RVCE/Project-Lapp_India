from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.uix.popup import Popup
from kivy.factory import Factory
from BACKEND_DB import validate_user_db
from BACKEND_DB import update_password
from BACKEND_PY import email_alert
from kivy.uix.screenmanager import ScreenManager, Screen
import re
# from kivy.uix.stacklayout import StackLayout
# from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from Push_Pop_screens import Push_Pop_screens
from kivy.properties import ObjectProperty

Window.size=(dp(1220),dp(780))

class Screen_Manager(Push_Pop_screens):
    access_level=int()
    plant_id=int()
    username='1'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def top_bar_values(self,user_access_level,user_plant_id,user_username):

        self.access_level=user_access_level
        self.plant_id=user_plant_id
        self.username=user_username

    def Userdetails(self):
        return [self.username,self.plant_id,self.access_level]

class Dashboard(Screen):
    def TopBar_Display(self):
        User_details=[]
        self.User_details=self.parent.Userdetails()
        self.ids.Access_Level_Display.text=str(self.User_details[2])
        self.ids.T_B_Plant_ID.text=str(self.User_details[1])
        self.ids.TOP_BAR_Username.text=str(self.User_details[0])


# class TopBar(BoxLayout):
#     pass

class SideBar(BoxLayout):

    def Dashboard_Change(self):
        if self.ids.Dashboard_Screen.text=='Dashboard  ': return
        self.ids.Inspection_Screen.text='Inspection  '
        self.ids.Report_Screen.text='Report  '
        self.ids.Admin_Screen.text='Admin  '

        if self.ids.Dashboard_Screen.initial_check==True:
            self.state_holder=self.ids.Dashboard_Screen
            self.ids.Dashboard_Screen.initial_check=False

        self.state_holder.colorcheck=True
        self.ids.Dashboard_Screen.colorcheck=False
        self.state_holder=self.ids.Dashboard_Screen

        match self.ids.Dashboard_Screen.text:
            case 'Dashboard: Info  ':
                self.parent.parent.parent.ids.manage_screen.push_without_pop('Dashboard_Info')

    def Inspection_Change(self):
        if self.ids.Inspection_Screen.text=='Inspection  ': return
        self.ids.Dashboard_Screen.text='Dashboard  '
        self.ids.Report_Screen.text='Report  '
        self.ids.Admin_Screen.text='Admin  '

        if self.ids.Dashboard_Screen.initial_check==True:
            self.state_holder=self.ids.Dashboard_Screen
            self.ids.Dashboard_Screen.initial_check=False

        self.state_holder.colorcheck=True
        self.ids.Inspection_Screen.colorcheck=False
        self.state_holder=self.ids.Inspection_Screen

        match self.ids.Inspection_Screen.text:
            case 'Inspection: Export  ':
                self.parent.parent.parent.ids.manage_screen.push_without_pop('Inspection_Export')

            case 'Inspection: Import  ':
                self.parent.parent.parent.ids.manage_screen.push_without_pop('Inspection_Import')


            case 'Inspection: Modify  ':
                UserDetails=self.parent.parent.parent.parent.Userdetails()
                self.parent.parent.parent.ids.manage_screen.push_confidential('Inspection_Modify',UserDetails[2],['2','3'])

    def Report_Change(self):
        if self.ids.Report_Screen.text=='Report  ': return
        self.ids.Dashboard_Screen.text='Dashboard  '
        self.ids.Inspection_Screen.text='Inspection  '
        self.ids.Admin_Screen.text='Admin  '

        if self.ids.Dashboard_Screen.initial_check==True:
            self.state_holder=self.ids.Dashboard_Screen
            self.ids.Dashboard_Screen.initial_check=False

        self.state_holder.colorcheck=True
        self.ids.Report_Screen.colorcheck=False
        self.state_holder=self.ids.Report_Screen

        match self.ids.Report_Screen.text:
            case 'Report: Export  ':
                self.parent.parent.parent.ids.manage_screen.push_without_pop('Report_Export')


            case 'Report: Import  ':
                self.parent.parent.parent.ids.manage_screen.push_without_pop('Report_Import')


            case 'Report: Modify  ':
                UserDetails=self.parent.parent.parent.parent.Userdetails()
                self.parent.parent.parent.ids.manage_screen.push_confidential('Report_Modify',UserDetails[2],['2','3'])


    def Admin_Change(self):
        if self.ids.Admin_Screen.text=='Admin  ': return
        self.ids.Dashboard_Screen.text='Dashboard  '
        self.ids.Inspection_Screen.text='Inspection  '
        self.ids.Report_Screen.text='Report  '

        if self.ids.Dashboard_Screen.initial_check==True:
            self.state_holder=self.ids.Dashboard_Screen
            self.ids.Dashboard_Screen.initial_check=False

        self.state_holder.colorcheck=True
        self.ids.Admin_Screen.colorcheck=False
        self.state_holder=self.ids.Admin_Screen

        match self.ids.Admin_Screen.text:
            case 'Admin: Users  ':
                UserDetails=self.parent.parent.parent.parent.Userdetails()
                self.parent.parent.parent.ids.manage_screen.push_confidential('Admin_Users',UserDetails[2],['3'])

        # self.ids.Dashboard_Screen.text='Dashboard'

class App_design(App):
    Run_file = ObjectProperty(None)
    def build(self):
        self.icon = 'Design_considerations/Images/App_Icon.png'
        self.Run_file=Screen_Manager()
        return self.Run_file

App_design().run()
    # shirishkumar.lapp@gmail.com
    # tabrez.lapp@gmail.com
