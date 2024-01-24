import tkinter as tk
import tkinter.ttk as ttk
from db.db import User, Product

window = tk.Tk()
window.geometry("960x640")

frm_centre = tk.Frame(
    master=window,
    borderwidth=1,
    relief="solid",
    highlightcolor="red",
    border=5,
    )


frm_dir= tk.Frame(master=frm_centre,
                     width = 1800,
                     height = 900)


columns = ("num", "name", "product","quantity","time")
tree = ttk.Treeview(master=frm_dir,columns=columns, show="headings")


 
tree.heading("num", text="Номер заказа")
tree.heading("name", text="Имя клиента")
tree.heading("product", text="Название товара")
tree.heading("quantity", text="Количество")
tree.heading("time", text="Оставшийся срок")
 

for string in Product.all():
   tree.insert("", tk.END, values=string)

scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command=tree.yview)
tree.config(yscrollcommand=scrollbar.set)

add_bt = tk.Button(master =frm_dir,text ="Добавить")
edit_bt = tk.Button(master =frm_dir,text ="Изменить")
del_bt = tk.Button(master =frm_dir,text = "Удалить")
back_bt = tk.Button(master =frm_dir,text = "Назад")

def Add(event):
   frm_dir.pack_forget()

def Back(event):
   frm_dir.pack_forget()
   #frm_lofin.pack()

tree.pack(fill=tk.BOTH, expand=1)
frm_centre.pack()
frm_dir.pack()
add_bt.pack()
edit_bt.pack()
del_bt.pack()
back_bt.pack()
scrollbar.pack(side=tk.RIGHT, fill=tk.Y, in_=frm_dir)
add_bt.bind("<Button-1>", Add)
back_bt.bind("<Button-1>", Back)


window.mainloop() 