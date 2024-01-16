import os
# import tkinter
from tkinter import *


def banner():  # создаем функцию вызова баннера
    # создаем окно баннера

    # корневой элемент
    root = Tk()
    root.title("Диагностика сети")
    root.geometry("+100+250")  # смещение окна по осям
    root.resizable(False, False)  # убираем функцию ресайза окна
    root.after(4000, lambda: root.destroy())  # баннер закрывается через 4 сек

    # дочерние элементы внутри корневого
    but1 = Button(root, text="Завершить", command=exit)
    lab = Label(root, text='Обрыв соединения. Вероятно, отвалилась сеть')

    # метод упаковки окна grid
    lab.grid(row=0, columnspan=2, ipady=10, ipadx=10)
    but1.grid(row=1, columnspan=2, padx=5, pady=10)

    root.mainloop()


hostname = '213.180.204.8'  # ya.ru
def mine():
# # запускаем бесконечный цикл опросов, если нулевые ответы ping
#     a = 1
#     while a == 1:
#         response = os.system("ping -c 1 " + hostname)
#         print(response)
#         if response != 0:
#             print(response)
#             banner()
    response = os.system("ping -c 4 " + hostname)
    print(response)
    if response != 0:
        print(response)
        banner()


if __name__ == "__main__":
    mine()
