from cgitb import text
from lib2to3.pgen2.token import RPAR
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

txt = Text(root, width= 30, height= 5) #텍스트 창이 만들어짐
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30) #한줄로 입력 받을 때
e.pack()
e.insert(0, "한줄만 입력해요")

def btncmd():
    #내용 출력
    print(text.get("1.0",END)) # 1  : 첫번째 라인을 의미  0 : 0번쨰 column 위치  
    print(e.get())

    #내용 삭제 
    txt.delete("1.0",END)
    e.delete()

btn = Button(root, text="클릭", command= btncmd)
btn.pack()

root.mainloop()