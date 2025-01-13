from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

class u_wight(object):
    def __init__(self):
        self.color = get_color_from_hex('#000000')

class u_label(Label, u_wight):
    def __init__(self,**kwargs):
        super(u_label, self).__init__()
        for key,value in kwargs.items():
            self.__setattr__(key,value)
class U_button(Button, u_wight):
    def __init__(self,**kwargs):
        super(U_button, self).__init__()
        for key,value in kwargs.items():
            self.__setattr__(key,value)