# kivy modules first, if not Kivy may cause problems
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
kivy.require('1.10.0')

# common modules
import sys
import os
import time
import signal
from multiprocessing import Process

# Flask modules
from flask import Flask

# wsgi (Web Server Gateway Interface) modules
import eventlet
from eventlet import wsgi

# async server setup
app = Flask(__name__)

def signal_handler(signal, frame):
    print(" CTRL + C detected, exiting ... ")
    exit(0)


# kivy gui classes ######################################################
class MainScreen(Screen):
    def __init__(self, **kwargs):
        self.name="MAIN SCREEN"
        super(Screen, self).__init__(**kwargs)

class MainApp(App):
    MainScreenTitle = "MainScreen title"
    MainScreenLabel = "MainScreen label"
    MessageButtonEnter = "START"
    MessageButtonExit = "EXIT"

    def start_Flask(self):
        print("Starting Flask...")
        wsgi.server(eventlet.listen(('', 5000)), app)     # deploy as an eventlet WSGI server

    def stop(self):
        print("terminating Flask and exiting...")
        global p1
        p1.terminate()
        exit(1)

    def start(self):
        print("starting Flask as process...")
        global p1
        p1 = Process(target=self.start_Flask) # assign Flask to a process
        p1.daemon = True
        p1.start()  #launch Flask as separate process

    def build(self):
        sm = Builder.load_string("""

ScreenManager
    MainScreen:
        size_hint: 1, .7
        auto_dismiss: False
        title: app.MainScreenTitle
        title_align: "center"

        BoxLayout:
            orientation: "vertical"
            Label:
                text: app.MainScreenLabel
            BoxLayout:
                orientation: "horizontal"
                spacing: 10
                size_hint: 1, .5
                Button:
                    text: app.MessageButtonEnter  # start app
                    on_press:
                        app.start()
                Button:
                    text: app.MessageButtonExit  # exit app
                    on_press:
                        app.stop()

        """)

        return sm


# main ################################################
if __name__ == '__main__':

    #CTRL+C signal handler
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    MainApp().run()   # run Kivy app
