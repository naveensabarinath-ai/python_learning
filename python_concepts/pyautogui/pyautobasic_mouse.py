import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2


def confirmed(prompt):
	return input(f"{prompt} (y/N): ").strip().lower() == "y"


def main():
	print("Mouse operations: move, click, double-click, drag, scroll, position")
	print("1 Move  2 Click  3 Double-click  4 Drag  5 Scroll  6 Show position")
	choice = input("Choose an operation: ").strip()

	if choice == "1":
		x = int(input("Target X coordinate: "))
		y = int(input("Target Y coordinate: "))
		if confirmed(f"Move the pointer to ({x}, {y})?"):
			pyautogui.moveTo(x, y, duration=1)
	elif choice in ("2", "3"):
		button = input("Button (left/right/middle): ").strip().lower()
		if button not in ("left", "right", "middle"):
			print("Unknown mouse button")
			return
		operation = "click" if choice == "2" else "double-click"
		if confirmed(f"Perform a {button} {operation}?"):
			if choice == "2":
				pyautogui.click(button=button)
			else:
				pyautogui.doubleClick(button=button)
	elif choice == "4":
		x = int(input("Drag destination X coordinate: "))
		y = int(input("Drag destination Y coordinate: "))
		if confirmed(f"Drag with the left button to ({x}, {y})?"):
			pyautogui.dragTo(x, y, duration=1, button="left")
	elif choice == "5":
		amount = int(input("Scroll clicks (positive=up, negative=down): "))
		if confirmed(f"Scroll by {amount} clicks?"):
			pyautogui.scroll(amount)
	elif choice == "6":
		print(f"Current pointer position: {pyautogui.position()}")
	else:
		print("Unknown operation")


if __name__ == "__main__":
	main()
