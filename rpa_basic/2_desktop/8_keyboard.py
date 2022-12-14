import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("Nadocoding", interval= 0.25)
# pyautogui.write("나도코딩") #pyautogui에서는 한글 입력이 안됨
# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"],interval=0.25)

# 특수문자
# shift 4 -> $
# pyautogui.keyDown("shift") # shift 키를 누른 상태에서
# pyautogui.press("4") # 숫자 4를 입력하고
# pyautogui.keyUp("shift") # shift 키를 뗀다

# 조합키(Hot key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") # press("a")
# pyautogui.keyUp("ctrl") # Ctrl + A

# 간편키 조합
# pyautogui.hotkey("ctrl", "alt", "shift" , "a")
# Ctrl 누르고 > Alt 누르고 > Shift 누르고 > A 누르고 > A 떼고 > Shift 떼고 > Alt 떼고 > Ctrl 떼고 
# pyautogui.hotkey("ctrl", "a")

import pyperclip
# pyperclip.copy("나도코딩") # "나도코딩" 글자를 클립보드에 저장 
# pyautogui.hotkey("ctrl","v") # 클리보드에 있는 내용 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

my_write("나도코딩")

# 자동화 프로그램 종료
# win : ctrl + alt + del
# Mac : cmd + shift + option + q