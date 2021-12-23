import pyautogui

# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash.png")
# pyautogui.moveTo(trash_icon)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

#여러개의 동일 아이콘이 화면에 있을 때, 동시에 모두 클릭 - pyautogui.locateAllOnScreen
# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration=0.5)

# 여러개 동일 아이콘 중에서 맨 처음 하나만 동작시킬 때 - pyautogui.locateOnScreen
# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 속도 개선
#1. GrayScale - 30% 속도 개선

# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)


#2. 범위 지정

# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True, region=(1688, 686, 1911-1688, 100))
# pyautogui.moveTo(trash_icon)

# pyautogui.mouseInfo()

#3. 정확도 조정, need to install opencv-python (pip install opencv-python)

# run_btn = pyautogui.locateOnScreen("run_btn.png", grayscale=True, confidence = 0.9) # 90% accuracy
# pyautogui.moveTo(run_btn)

#4 자동화 대상이 바로 보여지지 않는 경우
#1. 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else: 
#     print("Not found")

# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("Not found")

# pyautogui.click(file_menu_notepad)

#2. 일정 시간 동안 기다리기 (timeout)
import time
import sys


# timeout = 10 # 10초 대기
# start = time.time()
# file_menu_notepad = None

# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time()
#     if end -start > timeout:
#         print("시간 종료")
#         sys.exit()

# pyautogui.click(file_menu_notepad)

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end -start > timeout:
            break
    return target


def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}).Terminate program.")
        sys.exit()

my_click("file_menu_notepad.png", 10)