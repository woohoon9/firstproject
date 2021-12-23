import pyautogui

# print("it's staring soon")
# pyautogui.countdown(3)
# print("start automation")

# pyautogui.alert("Failed in the automation", "Alert")
# result = pyautogui.confirm("Do you want to proceed?", "Confirm")
# print(result)

# result = pyautogui.prompt("Please enter the file name", "Input the file name")
# print(result)

result = pyautogui.password("Enter password")# 암호 입력
print(result)