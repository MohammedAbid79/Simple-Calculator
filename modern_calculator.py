from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

KV = '''
<CalculatorLayout>:
    orientation: root.orientation_mode
    padding: 20
    spacing: 20

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, None if root.orientation_mode == 'vertical' else 0.7
        height: self.minimum_height
        spacing: 10

        TextInput:
            id: number1
            hint_text: 'Number 1'
            input_filter: 'float'
            multiline: False
        Spinner:
            id: operation
            text: '+'
            values: ['+', '-', '*', '/', 'sqrt']
        TextInput:
            id: number2
            hint_text: 'Number 2 (ignored for sqrt)'
            input_filter: 'float'
            multiline: False
            disabled: operation.text == 'sqrt'
        Button:
            text: 'Calculate'
            on_press: root.calculate()
        Label:
            id: result
            text: root.result_text
            font_size: '20sp'

    Button:
        text: 'Toggle Orientation'
        size_hint: None, None
        size: 160, 40
        on_press: root.toggle_orientation()
        pos_hint: {'center_y': 0.5}
'''

class CalculatorLayout(BoxLayout):
    result_text = StringProperty('')
    orientation_mode = StringProperty('vertical')

    def calculate(self):
        try:
            num1 = float(self.ids.number1.text)
        except ValueError:
            self.result_text = 'Invalid first number'
            return
        op = self.ids.operation.text
        if op != 'sqrt':
            try:
                num2 = float(self.ids.number2.text)
            except ValueError:
                self.result_text = 'Invalid second number'
                return
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                self.result_text = 'Cannot divide by zero'
                return
            result = num1 / num2
        elif op == 'sqrt':
            if num1 < 0:
                self.result_text = 'Cannot sqrt negative'
                return
            result = num1 ** 0.5
        else:
            self.result_text = 'Invalid operation'
            return
        self.result_text = str(result)

    def toggle_orientation(self):
        self.orientation_mode = 'horizontal' if self.orientation_mode == 'vertical' else 'vertical'

class ModernCalculatorApp(App):
    def build(self):
        Builder.load_string(KV)
        return CalculatorLayout()

if __name__ == '__main__':
    ModernCalculatorApp().run()
