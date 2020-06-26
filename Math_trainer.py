import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
kivy.require('1.11.1')
# Window.clearcolor = (0.15, 0.15, 0.15, 1)

class Home_page(Screen):
    def addition(self):
        screen_manager.current = "add"

    def subtraction(self):
        screen_manager.current = "sub"

    def multiplication(self):
        screen_manager.current = "mul"

    def division(self):
        screen_manager.current = "div"

class Add_page(Screen):
    pass

class Sub_page(Screen):
    pass

class Mul_page(Screen):
    pass

class Div_page(Screen):
    pass


graphics = Builder.load_file("Math_Trainer.kv")
screen_manager = ScreenManager()

screens = [Home_page(name="home"), Add_page(name="add"), Sub_page(name="sub"), Mul_page(name="mul"), Div_page(name="div")]
for screen in screens:
    screen_manager.add_widget(screen)

screen_manager.current = "home"

class Math_trainer(App):
    def build(self):
        return screen_manager

if __name__ == '__main__':
    Math_trainer().run()