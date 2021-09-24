from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window


Window.size = (500,700)
Builder.load_file('calc.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    def remove(self):
        prev = self.ids.calc_input.text

        if "Error - Press C" in prev:
            prev = ""

        prev = prev[:-1]
        if prev == "":
            self.ids.calc_input.text = '0'
        else:
            self.ids.calc_input.text = f'{prev}'

    def percentage(self):
        pass

    def button_press(self, button):
        prev = self.ids.calc_input.text

        if "Error - Press C" in prev:
            prev = ""

        if prev == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prev}{button}'

    def math_sign(self,sign):
        prev = self.ids.calc_input.text
        if prev[-1] not in "+-/*":
            self.ids.calc_input.text = f'{prev}{sign}'
        else:
            list_prev = list(prev)
            list_prev[-1] = sign
            prev = "".join(list_prev)
            self.ids.calc_input.text = f'{prev}'

    def invert_sign(self):
        prev = self.ids.calc_input.text
        if "-" in prev[0]:
            self.ids.calc_input.text = f'{prev.replace("-","")}'
        else:
            self.ids.calc_input.text = f'-{prev}'  
                   
    def float_pointer(self):
        prev = self.ids.calc_input.text
        num_list = prev.split("+")
        if "+" in prev and "." not in num_list[-1]:
            self.ids.calc_input.text = f'{prev}.'

        elif "." in prev:
            pass
        else:
            self.ids.calc_input.text = f'{prev}.'

    def equals(self):
        prev = self.ids.calc_input.text
        try:
            answer = eval(prev)
            self.ids.calc_input.text = f'{str(answer)}'
        except:
            self.ids.calc_input.text = "Error - Press C"

class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()