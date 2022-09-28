from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

frame= Frame(root)
frame.pack()

scsrollbar= Scrollbar(frame)
scsrollbar.pack(side="right", fill="y") 

#set이 없으면 스크롤을 내려도 다시 올라옴 
listbox = Listbox(frame,selectmode= "extended",height=10, yscrollcommand = scsrollbar.set)

for i in range(1,32):
    listbox.insert(END,str(i) + "일")
listbox.pack(side="left")

scsrollbar.config(command=listbox.yview)

root.mainloop()