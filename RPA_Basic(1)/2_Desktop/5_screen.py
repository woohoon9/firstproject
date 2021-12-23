import pyautogui
# 스크린샷 찍기
# img=pyautogui.screenshot()
# img.save("screenshot.png")
# pyautogui.mouseInfo()
# 25,12 67,172,242 #43ACF2
pixel = pyautogui.pixel(25, 12)
print(pixel)

print(pyautogui.pixelMatchesColor(25,12,(67,172,242,)))
print(pyautogui.pixelMatchesColor(25,12,pixel))
print(pyautogui.pixelMatchesColor(25,12,(67,172,243,)))