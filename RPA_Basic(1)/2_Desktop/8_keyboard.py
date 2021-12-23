import pyautogui

w = pyautogui.getWindowsWithTitle("Untitled")[0]
w.activate()

# pyautogui.write("12345")
# pyautogui.write("NadoCoding", interval = 0.5)
# pyautogui.write("나도코딩")



# pyautogui.write(["t","e","s", "t", "left", "left","right", "l", "a", "enter"], interval = 0.25) #automate the boring stuff with python

# 특수 문자
# shift 4 -> $

# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

#조합키(hot key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") # press("a")
# pyautogui.keyUp("ctrl") # Ctrl + A

# 간편 조합키

# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# pyautogui.hotkey("ctrl", "a")

# 키보드에서 한글 사용 : pip install pyperclip

import  pyperclip

# pyperclip.copy("나도코딩") #"나도코딩" 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl", "v") #클립보드에 있는 내용을 붙여넣기


def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("나도코딩")


# win: ctrl + alt +del - 자동화 프로그램 종료