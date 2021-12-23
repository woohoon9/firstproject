import pyautogui


# fw = pyautogui.getActiveWindow()
# print(fw.title)
# print(fw.size)
# print(fw.left, fw.top, fw.right, fw.bottom)

# pyautogui.click(fw.left +25, fw.top + 20)

# for w in pyautogui.getAllWindows():
#     print(w)

# for w in pyautogui.getWindowsWithTitle("Untitled"):
#     print(w)


w = pyautogui.getWindowsWithTitle("Untitled")[0]
print(w)
if w.isActive == False: # 현재 활성화 되지 않았다면, 화면 뒤쪽에 있다면
    w.activate() # 활성화 ( 맨 앞으로 가져 오기)

if w.isMaximized == False:
    w.maximize()

pyautogui.sleep(1)

# if w.isMinizzed == False:
#     w.minimize()

w.restore() # 화면 원복

w.close() # 윈도우 닫기

