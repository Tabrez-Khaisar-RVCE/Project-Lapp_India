from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.uix.popup import Popup
from kivy.factory import Factory
from BACKEND_DB import validate_user_db
from BACKEND_DB import update_password
from BACKEND_PY import email_alert
import re
# from kivy.uix.stacklayout import StackLayout
# from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from Push_Pop_screens import Push_Pop_screens
from kivy.properties import ObjectProperty
<<<<<<< Updated upstream
<<<<<<< Updated upstream
Window.size = (dp(1220), dp(780))

=======
=======
>>>>>>> Stashed changes

Window.size=(dp(1220),dp(780))
>>>>>>> Stashed changes

class Screen_Manager(Push_Pop_screens):
    pass


<<<<<<< Updated upstream
<<<<<<< Updated upstream
class LAPP_OLFLEX_Connect(App):
=======
=======
>>>>>>> Stashed changes
class LoginPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user_kv(self):
        email_id = self.ids.Username_text_input.text
        user_pwd = self.ids.Password_text_input.text
        validated = validate_user_db(email_id, user_pwd)
        if validated[0] == True and validated[1]==True:
            self.parent.parent.push_without_pop('Dashboard') #Moves to Dashboard screen
            global glb_Access_Level
            global glb_Plant_ID
            global glb_Username
            glb_Access_Level = validated[4]
            glb_Plant_ID = validated[3]
            glb_Username = validated[2]
        elif validated[0] == False or validated[1]==False:
            self.ids.Login_error_text.text = 'Login credentials is/are invalid' #Email or/and Password is False


class Change_pwd(Popup):
    Otp_validation=[]
    email_id=''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def OTP_Send(self):
        self.email_id=self.ids.Email_ID_Forgotten_pwd.text
        validated = validate_user_db(self.email_id,False)

        # Checks if email id is available
        if validated[0] == True:
            self.ids.Email_ID_Forgotten_pwd.disabled=True
            self.Otp_validation=email_alert(self.email_id) # returns OTP. If error returns False and Error code

            # Check for errors
            if self.Otp_validation[0]==False and self.Otp_validation[1]==11001:
                self.ids.change_pwd_info.text='Error 11001. Bad Gateway'
                return
            elif self.Otp_validation[0]==True:
                self.ids.OTP_input.disabled=False
                self.ids.change_pwd_info.text='OTP sent.'
                self.ids.OTP_input.focus=True
            else:
                self.ids.change_pwd_info.text='System error.'

        elif validated[0] == False:
            self.ids.change_pwd_info.text='Email not available.'

    def OTP_Check(self):
        Otp_recieved=self.ids.OTP_input.text
        if Otp_recieved==self.Otp_validation[1]:
            self.ids.change_pwd_info.text='Alphanumeric password.'
            self.ids.Password_new.disabled=False
            self.ids.Password_confirm.disabled=False
            self.ids.Confirm_email_button.disabled=False
            self.ids.OTP_input.disabled=True
            self.ids.OTP_button.disabled=True
            self.ids.Password_new.focus=True

        elif Otp_recieved!=self.Otp_validation[1]:
            self.ids.change_pwd_info.text='Wrong OTP'

    def change_password_kv(self):
        new_password=self.ids.Password_new.text
        confirm_password=self.ids.Password_confirm.text

        if len(new_password)<8:
            self.ids.change_pwd_info.text='Minimum length: 8'
        elif not bool(re.search(r'\d', new_password)):
            self.ids.change_pwd_info.text='Password has to have integers'
        elif not bool(re.search(r'[a-zA-Z]', new_password)):
            self.ids.change_pwd_info.text='Password has to have alphabets'
        elif new_password==confirm_password:
            update_password(self.email_id,new_password)
            self.dismiss()
        elif new_password!=confirm_password:
            self.ids.change_pwd_info.text='Passwords do not match'


class Dashboard():

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def top_display(self):
        self.ids.Access_Level_Display.text=str(self.glb_Access_Level)

class App_design(App):
    Run_file = ObjectProperty(None)

    def build(self):
        self.icon = 'Design_considerations/Images/App_Icon.png'
        self.Run_file = Screen_Manager()
        return self.Run_file

App_design().run()
    # shirishkumar.lapp@gmail.com
