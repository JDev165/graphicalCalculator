from tkinter import *
from expression import Expression

# Don't forget to add Python function annotations


class GUI:
    def __init__(self, title="Python Calculator", size="290x230"):
        self._gui = Tk()
        self._title = title
        self._size = size
        placeholder = StringVar().set("Enter your expression")
        self._field = Entry(self._gui, textvariable=placeholder)
        self._expression = None
        self._positions = {' ( ': (2, 0), ' ) ': (2, 1), ' CE ': (2, 2), ' - ': (2, 3),
                           ' 7 ': (3, 0), ' 8 ': (3, 1), ' 9 ': (3, 2), ' ÷ ': (3, 3),
                           ' 4 ': (4, 0), ' 5 ': (4, 1), ' 6 ': (4, 2), ' x ': (4, 3),
                           ' 1 ': (5, 0), ' 2 ': (5, 1), ' 3 ': (5, 2), ' + ': (5, 3),
                           ' 0 ': (6, 0), ' . ': (6, 2), ' = ': (6, 3), }

    def create(self):
        self._configure()
        self._create_input_field()
        self._create_buttons()
        self._gui.mainloop()

    def _configure(self):
        self._gui.configure(background="black")
        self._gui.title(self._title)
        self._gui.geometry(self._size)

    def _create_input_field(self):
        self._field.grid(rowspan=2, columnspan=4, ipadx=49, ipady=12)

    def _create_buttons(self):
        for buttonText in self._positions.keys():
            button = Button(self._gui, text=buttonText, height=2,
                            width=1, command=lambda action=buttonText: self._button_action(action))
            colspan = 2 if buttonText == " 0 " else 1
            # sticky removes extra space btwn buttons
            button.grid(row=self._positions[buttonText][0],
                        column=self._positions[buttonText][1], columnspan=colspan, sticky="nsew")

    def _button_action(self, action):
        action = action.strip()
        if action == '=':
            final_expression = self._field.get()
            if final_expression == '':
                self._field.delete(0, END)
                self._field.insert(0, 'Invalid Expression')
            else:
                self._expression = Expression(final_expression)
                self._field.delete(0, END)
                self._field.insert(0, self._expression.evaluate())
                del self._expression
        elif action == 'CE':
            current = str(self._field.get())[:-1]
            self._field.delete(0, END)
            self._field.insert(0, str(current))
        else:
            current = self._field.get()
            self._field.delete(0, END)
            self._field.insert(0, str(current) + str(action))


def main():
    calculatorGUI = GUI()
    calculatorGUI.create()


if __name__ == "__main__":
    main()
