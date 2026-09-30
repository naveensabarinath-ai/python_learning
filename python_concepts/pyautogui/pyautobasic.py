import pyautogui

pyautogui.FAILSAFE = True
print("TEST START")

x = int(input("Enter target X coordinate: "))
y = int(input("Enter target Y coordinate: "))
confirmation = input(f"Move the mouse to ({x}, {y})? (y/N): ")

if confirmation.lower() == "y":
	pyautogui.moveTo(x, y, duration=3.0)
	pyautogui.click()
	#print(f"Mouse moved to ({x}, {y})")
else:
	#print("Mouse movement cancelled")
