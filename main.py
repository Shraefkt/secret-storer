import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
import datan
d = datan.database("details.txt")
d.load()
class WindowManager(ScreenManager):
    pass
class CreateAccountWindow(Screen):
    usn = ObjectProperty(None)
    pswd = ObjectProperty(None)
    def submit(self):
        if self.usn.text != "" and len(self.pswd.text) >= 8:
            d.add_user(self.usn.text,self.pswd.text)
            self.reset()
            self.login()
        else:
            create_error()
    def reset(self):
        self.usn.text = ""
        self.pswd.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

class LoginWindow(Screen):
    usn = ObjectProperty(None)
    pswd = ObjectProperty(None)
    def submit(self):
        if d.validate(self.usn.text,self.pswd.text):
            self.reset()
            sm.current = "secret"
        else:
            login_error()
    def reset(self):
        self.usn.text = ""
        self.pswd.text = ""
    def create(self):
        self.reset()
        sm.current = "create"


class SecretNoteWindow(Screen):
    s = ObjectProperty(None)
    def login(self):
        sm.current = "login"
        d.current_usern = None
        d.save()
        self.s.text = ""
    def edit_note(self):
        d.change_sec(self.s.text)
    def r(self):
        self.s.text = d.find_secret()
    def save_edits(self):
        d.change_sec(self.s.text)
def login_error():
    pop = Popup(title='Invalid Login',
                content=Label(text='Invalid username or password.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()
def create_error():
    pop = Popup(title='Invalid Details',
                content=Label(text='Username taken or password too short'),
                size_hint=(None, None), size=(400, 400))
    pop.open()

kv = Builder.load_file("my.kv")
sm = WindowManager()
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),SecretNoteWindow(name="secret")]
for screen in screens:
    sm.add_widget(screen)
sm.current = "login"
class MyApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    MyApp().run()
