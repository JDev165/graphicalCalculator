from tkinter import *

# Don't forget to add Python function annotations


class GUI:
    def __init__(self, title="Python Calculator", size="270x150"):
        self._gui = Tk()
        self._title = title
        self._size = size
        self._result = None
        self._expression = None
        self._positions = {' 0 ': (1, 0), ' 1 ': (
            1, 1), ' 2 ': (1, 2), ' 3 ': (1, 3), ' 4 ': (2, 0), ' 5 ': (2, 1),
            ' 6 ': (2, 2), ' 7 ': (2, 3), ' 8 ': (2, 4), ' 9 ': (3, 0)}

    def create(self):
        self._configure()
        self._create_input_field()
        self._create_number_buttons()

        self._gui.mainloop()

    def _configure(self):
        self._gui.configure(background="black")
        self._gui.title(self._title)
        self._gui.geometry(self._size)

    def _create_input_field(self):
        placeholder = StringVar()
        placeholder.set("Enter your expression")
        field = Entry(self._gui, textvariable=placeholder)
        field.grid(columnspan=4, ipadx=40)

    def _create_number_buttons(self):
        for number in range(0, 10):
            number = " " + str(number) + " "
            button = Button(self._gui, text=number, fg='black',
                            bg='red', height=1, width=7)
            button.grid(row=self._positions[number]
                        [0], column=self._positions[number][1])

    def _set_input_field(self):
        pass


def main():
    calculatorGUI = GUI()
    calculatorGUI.create()


if __name__ == "__main__":
    main()
