import tkinter as tk
from tkinter.messagebox import showinfo, showerror
from tkinter import ttk

auth_win = tk.Tk()
auth_win.geometry('600x600')

formx = 250
formy = 200
entry_width = 20
users=[
    {'login': 'admin', 'password': 'admin'},
    {'login': 'rody', 'password': '1234'},
    {'login': '1', 'password': '1'}
]

def auth():
    log = login.get()
    pasw = password.get()
    for user in users:
        if user.get('login') == log and user.get('password') == pasw:
            showinfo('Поздравляем','ВЫ ВОШЛИ')
            auth_win.withdraw()
            admin_win.deiconify()
            return
    showerror('ошибка','вы не вошли')


tk.Label(auth_win, text='логин').place(x=formx, y=formy)
login = tk.Entry(auth_win, width=entry_width)
login.place(x=formx-30, y=formy+30)

tk.Label(auth_win, text='пароль').place(x=formx, y=formy+60)
password = tk.Entry(auth_win, width=entry_width)
password.place(x=formx-30, y=formy+80)

tk.Button(auth_win, text='войти', command=auth).place(x=formx, y=formy+120)

admin_win = tk.Tk()
admin_win.geometry('1300x900+0+0')
admin_win.withdraw()

formax = 300
formay = 400

tk.Label(admin_win, text='Имя клиента').place(x=50, y=0)
name_client = tk.Entry(admin_win, width=entry_width)
name_client.place(x=50, y=30)

tk.Label(admin_win, text='Вид оргтехники').place(x=50, y=80)
vid_tech = tk.Entry(admin_win, width=entry_width)
vid_tech.place(x=50, y=110)

tk.Label(admin_win, text='Модель').place(x=50, y=160)
model = tk.Entry(admin_win, width=entry_width)
model.place(x=50, y=190)

tk.Label(admin_win, text='Описание проблемы').place(x=50, y=240)
problem = tk.Entry(admin_win, width=entry_width)
problem.place(x=50, y=270)

tk.Label(admin_win, text='номер телефона').place(x=50, y=320)
number = tk.Entry(admin_win, width=entry_width)
number.place(x=50, y=350)

tk.Label(admin_win, text='ответственный').place(x=50, y=400)
human = tk.Entry(admin_win, width=entry_width)
human.place(x=50, y=430)

tk.Label(admin_win, text='комментарий').place(x=50, y=480)
comments = tk.Entry(admin_win, width=entry_width)
comments.place(x=50, y=510)

columns=['Имя клиента', 'Вид оргтехники', 'Модель', 'Описание проблемы', 'номер телефона', 'ответственный', 'комментарий']

tree = ttk.Treeview(admin_win, show='headings', height=11, columns=columns)

for index, el in enumerate(columns):
    tree.column(index, width=150)
    tree.heading(el, text=el)
tree.place(x=200, y=10)
tk.Button(admin_win, text='сохранить').place(x=formx, y=600)

tk.Button(admin_win, text='Взять в работу').place(x=formx, y=650)

tk.Button(admin_win, text='Завершить').place(x=350, y=600)

tk.Button(admin_win, text='Изменить описание проблемы').place(x=350, y=650)

tk.Button(admin_win, text='Добавить исполнителя').place(x=550, y=650)

tk.Button(admin_win, text='Изменить исполнителя').place(x=610, y=600)

tk.Button(admin_win, text='Добавить комментарий').place(x=450, y=600)

auth_win.mainloop()
