# controller
from tkinter import *
from tkinter.ttk import Combobox 
import test_generator
import test_screen

table_width_txt = None
table_height_txt = None
test_type_cmb_box = None
test_time_txt = None

def main_window_setup():
    window = Tk()
    window.geometry('700x400')
    window.title("Тест Бурдона")

    lbl = Label(window, text="Количество столбцов")
    lbl.grid(column=0, row=0)
    lbl.grid(padx=10, pady=10)
    global table_width_txt
    table_width_txt = Entry(window,width=10)
    table_width_txt.grid(column=1, row=0)
    lbl = Label(window, text="Количество строк")
    lbl.grid(column=0, row=1)
    lbl.grid(padx=10, pady=10)
    global table_height_txt
    table_height_txt = Entry(window,width=10)
    table_height_txt.grid(column=1, row=1)
    lbl = Label(window, text="Тип символов в таблице")
    lbl.grid(column=0, row=2)
    lbl.grid(padx=10, pady=10)
    global test_type_cmb_box
    test_type_cmb_box = Combobox(window)
    test_type_cmb_box['values'] = ('rus', 'num')
    test_type_cmb_box.current(0)
    test_type_cmb_box.grid(column=1, row=2, padx=10, pady=10)

    # lbl = Label(window, text="Время тестирования (в секундах)")
    # lbl.grid(column=0, row=3)
    # lbl.grid(padx=10, pady=10)
    # global test_time_txt
    # test_time_txt = Entry(window,width=10)
    # test_time_txt.grid(column=1, row=3)

    btn = Button(window, text="Сгенерировать тест", command=(lambda : switch_to_test_gen()))
    btn.grid(column=1, row=4, padx=10, pady=10)

    window.mainloop()


def switch_to_test_gen():
    global table_width_txt
    global table_height_txt
    global test_type_cmb_box
    global test_time_txt

    # test_screen.generate_test_window(int(table_width_txt.get()), int(table_height_txt.get()), test_type_cmb_box.get(), int(test_time_txt.get()))
    test_screen.generate_test_window(int(table_width_txt.get()), int(table_height_txt.get()), test_type_cmb_box.get())


if __name__ == '__main__':
    main_window_setup()
