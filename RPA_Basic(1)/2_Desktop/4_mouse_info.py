import pyautogui
# pyautogui.mouseInfo()
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.5

for i in range(5):
    pyautogui.move(100,100)
    pyautogui.sleep(1)