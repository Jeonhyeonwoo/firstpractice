from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

Label(root, text="메뉴를 선택하세요").pack()

burger_Var = IntVar() #여기에 int형으로 값을 저장 
btn_buger1 = Radiobutton(root, text="햄버거", value= 1 , variable= burger_Var)
btn_buger2 = Radiobutton(root, text="치즈버거", value= 2 , variable= burger_Var)
btn_buger3 = Radiobutton(root, text="치킨버거", value= 3 , variable= burger_Var)

btn_buger1.pack()
btn_buger2.pack()
btn_buger3.pack()

Label(root, text="음료를 선택하세요").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라" , value= "콜라" , variable= drink_var)
btn_drink2 = Radiobutton(root, text="사이다" , value= "사이다" , variable= drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_Var.get()) #햄버거 중 선택된 라디오 항목의 값(Value)을 출력
    print(drink_var.get())


btn = Button(root, text="주문", command= btncmd)
btn.pack()

root.mainloop()