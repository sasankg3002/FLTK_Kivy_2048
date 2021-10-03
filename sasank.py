import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class GridLayoutExample(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        for i in range(0,16):
            l = Label(text = "")

class Game2048App(App):
    pass

Game2048App().run()