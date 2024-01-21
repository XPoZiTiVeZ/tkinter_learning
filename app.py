import tkinter as tk
from db.db import User


window = tk.Tk()
window.geometry("960x640")

frm_login = tk.Frame(
    master=window,
    borderwidth   =1,
    relief        ="solid",
    highlightcolor="red",
    border        =1,
    width         =300,
    height        =300
)

lbl_login = tk.Label(
    master =frm_login,
    text   ="Логин:",
    width  =20,
    height =5
)
ent_login = tk.Entry(
    master =frm_login,)
lbl_password = tk.Label(
    master =frm_login,
    text   ="Пароль:"
)
ent_password = tk.Entry(
    master = frm_login
)
btn_login = tk.Button(
    master =frm_login,
    text   ="Войти"
)
btn_exit = tk.Button(
    master =frm_login,
    text   ="Выйти"
)

frm_login.pack(anchor="nw")
frm_login.pack_propagate(False)
lbl_login.pack()
ent_login.pack()
lbl_password.pack()
ent_password .pack()
btn_login.pack()
btn_exit.pack()



def login(event):
    lgn = ent_login.get()
    pwd = ent_password.get()
    user = User.authenticate(lgn, pwd)
    if user != None:
        if user.role == "Директор":
            frm_login.pack_forget()
        elif user.role == "Администратор":
            frm_login.pack_forget()
        else:
            print(user.role)
    else:
        ent_password.delete(0,"end")
        ent_password.config(bg="#EE0000")
        window.focus()
    


btn_login.bind("<Button-1>",   login)
btn_exit.bind("<Button-1>",    lambda _: window.destroy())
ent_password.bind("<FocusIn>", lambda _: ent_password.config(bg="white"))


window.mainloop() 