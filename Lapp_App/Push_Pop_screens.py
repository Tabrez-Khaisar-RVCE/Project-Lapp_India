from kivy.uix.screenmanager import ScreenManager

class Push_Pop_screens(ScreenManager):
    screen_stack=[]
    def push(self,screen_name):
        if screen_name not in self.screen_stack:
            self.screen_stack.append(self.current)
            self.transition.direction='left'
            self.current=screen_name

    def pop(self):
        if len(self.screen_stack)>=1:
            screen_name = self.screen_stack[-1]
            del self.screen_stack[-1]
            self.transition.direction='right'
            self.current=screen_name

# To navigate into the root directory, use "cd /"
# To navigate to your home directory, use "cd" or "cd ~"
# To navigate up one directory level, use "cd .."
# To navigate to the previous directory (or back), use "cd -"
