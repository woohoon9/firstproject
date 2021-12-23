import pyautogui
import sys

pyautogui.hotkey("win", "r")# 단축기 : win+r 입력
pyautogui.write("mspaint") # 프로그램 명 입력
pyautogui.press("enter") # 엔터키 입력

 # 그림판 나타날때 까지 2 초 대기
pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle("Untitled - Paint")[0] # 그림판이 한개만 띄워져 있다고 가정
if window.isMaximized == False:
    window.maximize()


# 글자 버튼 클릭
btn_text = pyautogui.locateOnScreen("text.png")
if btn_text:
    pyautogui.click(btn_text)
else:
    print("failed to find")
    sys.exit()

# 흰 영역 클릭n
pyautogui.click(200,200, duration = 0.5)
# btn_brush = pyautogui.locateOnScreen("brush.png", confidence = 0.8)
# pyautogui.click(btn_brush.left-200, btn_brush.top+50, duration = 0.5)

import  pyperclip

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("참 잘 했어요")

# 5초 대기
pyautogui.sleep(5)

# 프로그램 종료
window.close()
pyautogui.sleep(0.5)
pyautogui.press("n") # 저장하지 않음


