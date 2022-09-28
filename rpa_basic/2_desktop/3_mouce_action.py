import pyautogui
# pyautogui.sleep(3) # 3초 대기
# print(pyautogui.position())

# pyautogui.click(64,17, duration=1) # 1초 동안 (64, 17) 좌표를 이동 후  마우스 클릭
# pyautogui.click()
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks=500)

# pyautogui.moveTo(200,200)
# pyautogui.mouseDown() # 마우스 버튼 누른 상태
# pyautogui.moveTo(300,300)
# pyautogui.mouseUp()

pyautogui.sleep(3)
# # pyautogui.rightClick()
# # pyautogui.middleClick()

# pyautogui.moveTo(1114,349)
# pyautogui.drag(100,0,duration = 0.25) # 너무 빠른 동작으로 drag 수행이 안될때는 duration
# pyautogui.dragTo(1514, 349, duration=0.25) # 절대 좌표 기준으로 x,y 로 드래그 

pyautogui.scroll(300) # 양수이면 위 방향으로 음수이면 아래 방향으로 300만큼 스크롤