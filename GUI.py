from tkinter import *
import tkinter.font as tk_font
from demo_2 import *


def update_listbox(tasks):
    delete_all_tasks()
    for task in tasks:
        to_do_list.insert(0, task)

def add_task(event):
    task = to_do_task.get()
    to_do_task.delete(0, END)

    if task and task != None :
        add_new_task(task) # Вызов функции добавления задания
        update_listbox(task_list)

def delete_task(event):
    selected = to_do_list.curselection()
    if selected:
        selected_task = to_do_list.get(selected)
        del_old_task(selected_task) # Вызов функции удаления старого задания
        update_listbox(task_list)

r = False
def sort_tasks(event):
    global r
    r = not r
    sort_all_tasks(r) # Вызов функции сортировки задания по возрастанию/убыванию
    update_listbox(task_list)

def delete_all_tasks(event=None):
    if event:
        del_all_tasks() # Вызов функции удаления всех заданий
    to_do_list.delete(0, END)

WIDTH = 500
HEIGHT = 450

window = Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")
window.title("Список задач!")

font_style = tk_font.Font(family="Verdana", size=10)
frame = Frame(window, bd=10)
frame.place(relx=0.05,
            rely=0.1,
            relwidth=0.9,
            relheight=0.8)
###########################################
# Добавление кнопок в колонку слева

# Кнопка добавления заданий
add_button = Button(frame, text="Добавить", font=font_style)
add_button.place(relx=0,
                 rely=0,
                 relwidth=0.25,
                 relheight=0.1)
add_button.bind("<Button-1>", add_task)
# Кнопка удаления заданий
del_button = Button(frame, text="Удалить", font=font_style)
del_button.place(relx=0,
                 rely=0.2,
                 relwidth=0.25,
                 relheight=0.1)
del_button.bind("<Button-1>", delete_task)
# Кнопка сортировки заданий по дате
sort_button = Button(frame, text="Сортировать", font=font_style)
sort_button.place(relx=0,
                  rely=0.4,
                  relwidth=0.25,
                  relheight=0.1)
sort_button.bind("<Button-1>", sort_tasks)
# Добавление кнопок в колонку слева
del_all_button = Button(frame,
                        text="Удалить\nвсе",
                        font=font_style)
del_all_button.place(relx=0,
                     rely=0.8,
                     relwidth=0.25,
                     relheight=0.2)
del_all_button.bind("<Button-1>", delete_all_tasks)
###########################################



###########################################
# Добавление элементов в колонку справа
to_do_task = Entry(frame, font=font_style)
to_do_task.place(relx=0.3,
                 rely=0,
                 relwidth=0.6,
                 relheight=0.1)

# Создание полосы прокрутки
scrollbar = Scrollbar(frame)
# Размещение полосы прокрутки
scrollbar.place(relx=0.9,
                rely=0.2,
                relwidth=0.05,
                relheight=0.8)
# Создание списка задач
to_do_list = Listbox(frame,
                        font=font_style,
                        yscrollcommand=scrollbar.set)
# Размещение списка задач
to_do_list.place(relx=0.3,
                 rely=0.2,
                 relwidth=0.6,
                 relheight=0.8)
# Задание команды для просмотра списка задач
# с помощью полосы прокрутки
scrollbar.config(command=to_do_list.yview)
###########################################

window.mainloop()
