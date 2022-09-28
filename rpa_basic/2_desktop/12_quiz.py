import pyautogui
from random import *
import sys
import pyperclip

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

pyautogui.hotkey("win","r")
pyautogui.write("mspaint")
pyautogui.keyDown("enter")
pyautogui.keyUp("enter")

pyautogui.sleep(2)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]

if w.isMaximized == False: # 현재 최대화가 되지 않았다면
    w.maximize() # 최대화


text_icon = pyautogui.locateOnScreen("text_icon.png")
pyautogui.click(text_icon)
#pyautogui.click(200,200)
btn_brush = pyautogui.locateOnScreen("btn_brush.png")
pyautogui.click(btn_brush.left - 200 , btn_brush.top + 200)
pyautogui.sleep(2)

my_write("참 잘했어요")

pyautogui.sleep(5)
w.close()
pyautogui.sleep(0.5)
pyautogui.press("n")

