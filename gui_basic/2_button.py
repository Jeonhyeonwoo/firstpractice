from email.mime import image
from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text = "버튼1")
btn1.pack() #이걸 해줘야만 실제로 버튼이 보임 

btn2 = Button(root , padx=5, pady= 10, text="버튼2") #글자 크기에 비례한 크기 
btn2.pack()

btn3 = Button(root , padx=10, pady= 5, text="버튼2")
btn3.pack()

btn4 = Button(root, width= 10 , height=3 , text="버튼4") #고정크기
btn4.pack()

btn5 = Button(root, fg= "red", bg= "yellow", text="버튼5") #fg 글자 색상 bg 배경색상 
btn5.pack()

photo = PhotoImage(file="gui_basic/img.png")
btn6 = Button(root, image = photo)
btn6.pack() 

def btncmd():
    print("버튼이 클릭 되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()


root.mainloop()