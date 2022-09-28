import pyautogui
# # 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장 

# pyautogui.mouseInfo()
# 27,16 66,171,242 #42ABF2

pixel = pyautogui.pixel(27,16)
print(pixel)

# print(pyautogui.pixelMatchesColor(27,16,(66, 171, 242)))
# print(pyautogui.pixelMatchesColor(27,16,pixel))
print(pyautogui.pixelMatchesColor(27,16,(66, 171, 243)))