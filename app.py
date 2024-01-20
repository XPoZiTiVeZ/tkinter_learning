import tkinter as tk
from db.db import session, User


window = tk.Tk()

lbl_login    = tk.Label(text="Логин:")
ent_login    = tk.Entry()
lbl_password = tk.Label(text="Пароль:")
ent_password = tk.Entry()
btn_login    = tk.Button(text = "Войти" )
btn_exit     = tk.Button(text = "Выйти")

# Label - lbl - lbl_data
# Button - btn - btn_data
# Entry - ent - ent_data
# Text - txt - txt_data
# Frame - frm -frm_data 


lbl_login.pack()
ent_login.pack()
lbl_password.pack()
ent_password .pack()
btn_login.pack()
btn_exit.pack()


def knock_knock(event):
    lgn = ent_login.get()
    pwd = ent_password.get()
    user = User.authenticate(lgn, pwd)
    if user != None:
        if user.role == "Директор":
            print("Директор")
        elif user.role == "Администратор":
            print("Администратор")
        else:
            print("Обычный пользователь")
    else:
        ent_password.delete(0,"end")
        ent_password.config(bg="#EE0000")
        ent_password.focus_set()


btn_login.bind("<Button-1>",knock_knock)
btn_exit.bind("<Button-1>", lambda _: window.destroy())
ent_password.bind("<FocusIn>", lambda _: ent_password.config(bg="white"))


window.mainloop() 