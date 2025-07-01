import random
import threading
import tkinter
from tkinter import ttk, IntVar, X, NW

list_numbers = [random.randint(1,100) for i in range(15000)]

def bubble_sort(array, progress_var,window):
    for i in range(len(array)):
        progress_var.set(i)
        window.update_idletasks()
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


def handler_on_click_start(window):
    progress_var = IntVar()
    progressbar = ttk.Progressbar(variable=progress_var, maximum=len(list_numbers)-1)
    progressbar.pack(fill=X, padx=6, pady=6)

    label = ttk.Label(textvariable= progress_var)
    label.pack(anchor=NW, padx=6, pady=6)

    threading.Thread(target= bubble_sort, args=(list_numbers, progress_var, window)).start()




def main():

    window = tkinter.Tk()
    window.title('Hello Kara!')

    btn_start = ttk.Button(text='Start', width=50, command = lambda :handler_on_click_start(window))
    btn_start.pack()

    window.mainloop()

if __name__ == '__main__':
    main()