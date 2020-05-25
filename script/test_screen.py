from tkinter import *
import test_generator
import main
import analize
from datetime import datetime, date, time
from tkinter import messagebox  

statistics_list = []

window = None
clock = None
symbols = None
answers_count = None
correct_test_counter = None
wrong_test_counter = None
wrong_str_count = 0
passed_str_count = 0
t_width = 0
t_height = 0

after_id = ''
time_sek = 0

btn_matrix = []
btn_selected_matrix = []

class CallBtn:
    def __init__(self, x, y, btn):
        self.x = x
        self.y = y
        self.btn = btn
        self.isSelected = False
    def __call__(self):
        global symbols, correct_test_counter, wrong_test_counter
        # self.lbl.configure(text=f'Нажал на кнопку с координатами ({self.x}, {self.y})')
        # self.btn
        pt = symbols[0]
        if (self.y % 2 == 1):
            pt = symbols[1]
        # print(pt)
        # print(self.btn['text'])
        if (not self.isSelected):
            if (self.btn['text'] == pt):
                # print('good')
                correct_test_counter[self.y] += 1
            else:
                wrong_test_counter[self.y] += 1
                # print('bad')
            btn_selected_matrix[self.y][self.x] = True
            self.isSelected = True
            self.btn.configure(fg = 'white', bg = 'orange')
        else:
            if (self.btn['text'] == pt):
                correct_test_counter[self.y] -= 1
                # print('make worst')
            else:
                wrong_test_counter[self.y] -= 1
                # print('improved')
            btn_selected_matrix[self.y][self.x] = False
            self.isSelected = False
            self.btn.configure(fg = 'black', bg = 'white')


class FlagSet:
    def __init__(self, y):
        self.y = y
        self.isSelected = False
        self.isBad = False
    def __call__(self):
        global correct_test_counter, answers_count, wrong_test_counter, passed_str_count, wrong_str_count
        if (not self.isSelected):
            self.isSelected = True
            passed_str_count += 1
            if (wrong_test_counter[self.y] > 0 or correct_test_counter[self.y] != answers_count[self.y]):
                wrong_str_count += 1
                self.isBad = True
        else:
            self.isSelected = False
            passed_str_count -= 1
            if (self.isBad == True):
                wrong_str_count -= 1
                self.isBad = False


# def generate_test_window(table_width, table_height, test_type, time_in_seconds):
def generate_test_window(table_width, table_height, test_type):
    global t_width, t_height
    t_width = table_width
    t_height = table_height
    global time_sek, answers_count
    time_sek = 0
    global window
    window = Tk()
    window.geometry('700x400')
    window.title("Тест Бурдона")
    global symbols
    matrix, symbols, answers_count = test_generator.generate_test(test_type, table_width, table_height)

    lbl = Label(window, text="Нажимайте на кнопки, чтобы вычеркнуть букву.")
    lbl.grid(column=0, row=0)
    lbl = lbl = Label(window, text="Повторное нажатие отменит вычёркивание.")
    lbl.grid(column=0, row=1)
    lbl = Label(window, text=f'На нечётных строках вычёркивать: {symbols[0]}')
    lbl.grid(column=0, row=2)
    lbl = Label(window, text=f'На чётных строках вычёркивать: {symbols[1]}')
    lbl.grid(column=0, row=3)
    lbl = Label(window, text=f'Пройденные строки помечайте галочками справа')
    lbl.grid(column=0, row=4)
    lbl = Label(window, text=f'Пройденное время')
    lbl.grid(column=0, row=5)
    global clock
    clock = Label(window, text='00:00')
    clock.grid(column=0, row=6)
    btn = Button(window, text="Остановить тест", command=(lambda : stop()))
    btn.grid(column=0, row=7)

    global wrong_str_count, passed_str_count, correct_test_counter, wrong_test_counter, btn_matrix, btn_selected_matrix
    wrong_str_count = 0
    passed_str_count = 0
    correct_test_counter = [0 for i in range(table_width)]
    wrong_test_counter = [0 for j in range(table_width)]

    for i in range(table_height):
        btn_arr = []
        btn_sel_arr = []
        for j in range(table_width):
            btn = Button(window, text=matrix[i][j], height = 1, width = 2, bg = 'white')
            btn['command'] = CallBtn(j, i, btn)
            btn.grid(row=i+1, column=j+1)
            btn_arr.append(btn)
            btn_sel_arr.append(False)
            
        btn_selected_matrix.append(btn_sel_arr)
        btn_matrix.append(btn_arr)
        chk_state = BooleanVar()
        chk_state.set(False)
        chk = Checkbutton(window, var=chk_state)
        chk['command'] = FlagSet(i)
        chk.grid(row=i + 1, column=table_width + 2)
    
    tick()


def move_to_main_window(window):
    window.quit()
    main.main_window_setup()


def tick():
    global time_sek, after_id, window
    after_id = window.after(1000, tick)
    stamp_time = datetime.fromtimestamp(time_sek + 900000).strftime("%M:%S")
    clock.configure(text=str(stamp_time))
    #todo tick measuares for graphic
    time_sek += 1


def print_answers():
    global symbols, btn_matrix, t_width, t_height
    for i in range(t_height):
        for j in range(t_width):
            if (btn_matrix[i][j]['text'] == symbols[(i + 1) % 2]):
                if (btn_selected_matrix[i][j] == True):
                    btn_matrix[i][j].configure(fg = 'white', bg = 'green')
                else:
                    btn_matrix[i][j].configure(fg = 'white', bg = 'red')
            elif (btn_selected_matrix[i][j] == True):
                btn_matrix[i][j].configure(fg = 'white', bg = 'red')


def stop():
    global time_sek, after_id, window, wrong_str_count, passed_str_count
    messagebox.showinfo('Результаты', f'время в секундах {time_sek} || количество пройденных строк {passed_str_count} || количество ошибочных строк {wrong_str_count}')
    window.after_cancel(after_id)
    print_answers()
    # window.destroy()
    # make results
    # Results()
