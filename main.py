#!/usr/bin/python3

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import math

prev = ""

class ButtonEvent():
    def __init__(self, text, numbers):
        self.button = QPushButton(text)
        self.text = text
        self.numbers = numbers
        self.button.clicked.connect(lambda: self.executeExpression(self.text))

    def executeExpression(self, text):
        input_expr = self.numbers.text()
        global prev
        if prev == "=" and text.isdigit() == True:
            self.numbers.setText(text) 
        elif text == "=":
            output_expr = eval(input_expr)
            self.numbers.setText(str(output_expr))
        elif text == "C":
            self.numbers.setText("0")
        elif text == "x^y":
            self.numbers.setText(input_expr + "**")
        elif input_expr == "0":
            self.numbers.setText(text)
        else:
            self.numbers.setText(input_expr + text)
        prev = text


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.set_interface()

    def set_interface(self):
        numbers = QLineEdit("0")
        numbers.setAlignment(Qt.AlignRight)

        grid_layout = QGridLayout()

        grid_layout.addWidget(numbers, 0, 0, 1, 4)

        buttons_list = [
            "C", "x^y", "%", "/",
            "7", "8", "9", "*",
            "4", '5', "6", "-",
            "1", "2", "3", "+",
            ".", "0", "="
        ]
        
        r = 1
        c = 0
        for btn in buttons_list:
            button = ButtonEvent(str(btn), numbers)
            if btn == "=":
                grid_layout.addWidget(button.button, r, c, 1, 2)
            else:
                grid_layout.addWidget(button.button, r, c, 1, 1)           
            if c >= 3:
                c=0
                r+=1    
            else: 
                c+=1


        self.setLayout(grid_layout)
        self.show()
        self.setWindowTitle("Calculator")

    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = Calculator()
    sys.exit(app.exec_())











