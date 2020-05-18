# controller
from tkinter import *
import test_generator

class CallBtn:
    def __init__(self, x, y, lbl):
        self.x = x
        self.y = y
        self.lbl = lbl
    def __call__(self):
        self.lbl.configure(text=f'Нажал на кнопку с координатами ({self.x}, {self.y})')
        self.lbl.grid()


def window_setup():
    window.geometry('700x400')
    window.title("Hello World")

    btn = Button(window, text="Сгенерировать тест", command=(lambda: generate_btn_click(btn)))
    btn.grid(column=0, row=0)

    window.mainloop()


def generate_btn_click(temp_btn):
    table_width = 10
    table_height = 15

    temp_btn.grid_remove()
    btn = Button(window, text='На главное окно', command=reset_window_btn_click)
    btn.grid(column=0, row=0)

    matrix, symbols = test_generator.generate_test('rus', table_width, table_height)
    
    # code that should be reformated
    lbl = Label(window, text=f'Нажал на кнопку с координатами')
    lbl.grid(column=0, row=1)
    lbl.grid_forget()
    
    for i in range(table_height):
        for j in range(table_width):
            btn = Button(window, text=matrix[i][j], command=CallBtn(i, j, lbl))
            btn.grid(column=i + 1, row=j + 1)


def reset_window_btn_click():
    # todo button clearify
    window_setup()
    


if __name__ == '__main__':
    window = Tk()
    window_setup()
