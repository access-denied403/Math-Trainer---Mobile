import kivy
import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
kivy.require('1.11.1')

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
    answer = ObjectProperty(None)
    question = ObjectProperty(None)
    score = ObjectProperty(None)
    easy = ObjectProperty(None)
    medium = ObjectProperty(None)
    hard = ObjectProperty(None)
    
    def __init__(self, **kwargs):
    	super().__init__(**kwargs)
    	self.question.text = self.ask()

    def ask(self):
        if self.easy.active:
            self.num1 = random.randint(1, 9)
            self.num2 = random.randint(1, 9)
            return f"{self.num1} + {self.num2}"
        elif self.medium.active:
            self.num1 = random.randint(10, 99)
            self.num2 = random.randint(10, 99)
            return f"{self.num1} + {self.num2}"
        elif self.hard.active:
            self.num1 = random.randint(100, 999)
            self.num2 = random.randint(100, 999)
            return f"{self.num1} + {self.num2}"
    	
    
    def submit(self):
        if str(self.answer.text) == str(self.num1 + self.num2):
            self.score.text = str(int(self.score.text) + 1)
            self.answer.text = ""
            self.question.text = self.ask()    		
        else:
            self.score.text = str(int(self.score.text) - 1)
            self.answer.text = ""
            self.question.text = self.ask()


    def home(self):
        screen_manager.current = "home"



class Sub_page(Screen):
    answer = ObjectProperty(None)
    question = ObjectProperty(None)
    score = ObjectProperty(None)
    
    def __init__(self, **kwargs):
    	super().__init__(**kwargs)
    	self.question.text = self.ask()

    def ask(self):
    	self.num1 = random.randint(1, 9)
    	self.num2 = random.randint(1, 9)
    	return f"{self.num1} - {self.num2}"
    
    def submit(self):
    	if str(self.answer.text) == str(self.num1 - self.num2):
    		self.score.text = str(int(self.score.text) + 1)
    		self.answer.text = ""
    		self.question.text = self.ask()    		
    	else:
    		self.score.text = str(int(self.score.text) - 1)
    		self.answer.text = ""
    		self.question.text = self.ask()

    def home(self):
        screen_manager.current = "home"



class Mul_page(Screen):
    def home(self):
        screen_manager.current = "home"


class Div_page(Screen):
    def home(self):
        screen_manager.current = "home"


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
