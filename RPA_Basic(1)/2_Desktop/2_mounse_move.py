import pyautogui

#마우스 이동
# pyautogui.moveTo(200,100)
# pyautogui.moveTo(100,200, duration = 2)

# pyautogui.moveTo(100,100, duration = 0.5)
# pyautogui.moveTo(200,200, duration = 0.5)
# pyautogui.moveTo(300,300, duration = 0.5)

# pyautogui.move() # 상대좌표 움직임

# pyautogui.moveTo(100,100, duration = 0.5)
# print(pyautogui.position())
# pyautogui.move(100,100, duration = 0.5)
# print(pyautogui.position())
# pyautogui.move(100,100, duration = 0.5)
# print(pyautogui.position())

p = pyautogui.position()
print(p[0], p[1]) #x,y
print(p.x, p.y) #x,y