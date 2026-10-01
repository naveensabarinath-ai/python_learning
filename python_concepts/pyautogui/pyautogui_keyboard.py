import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2


HOTKEYS = {
	"1": ("Ctrl+S", ("ctrl", "s")),
	"2": ("Ctrl+C", ("ctrl", "c")),
	"3": ("Ctrl+V", ("ctrl", "v")),
	"4": ("Ctrl+Z", ("ctrl", "z")),
	"5": ("Ctrl+A", ("ctrl", "a")),
}


def confirm(prompt):
	return input(f"{prompt} (y/N): ").strip().lower() == "y"

def prepare_target():
	print("Switch to the target application; the operation starts in 3 seconds.")
	time.sleep(3)


def main():
	print("Keyboard operations: type text, press a key, send a hotkey, hold a key")
	print("1 Type text  2 Press a key  3 Hotkey  4 Hold a key briefly")
	choice = input("Choose an operation: ").strip()

	if choice == "1":
		text = input("Text to type: ")
		if confirm(f"Type {text!r} into the active application?"):
			prepare_target()
			pyautogui.write(text, interval=0.05)
	elif choice == "2":
		key = input("Key name (for example enter, tab, or esc): ").strip().lower()
		if confirm(f"Press {key!r} in the active application?"):
			prepare_target()
			pyautogui.press(key)
	elif choice == "3":
		for number, (name, _) in HOTKEYS.items():
			print(f"{number}. {name}")
		hotkey_choice = input("Choose a hotkey: ").strip()
		if hotkey_choice in HOTKEYS:
			name, keys = HOTKEYS[hotkey_choice]
			if confirm(f"Send {name} to the active application?"):
				prepare_target()
				pyautogui.hotkey(*keys)
		else:
			print("Unknown hotkey")
	elif choice == "4":
		key = input("Key to hold (for example shift): ").strip().lower()
		duration = float(input("Hold duration in seconds (0 to 5): "))
		if not 0 <= duration <= 5:
			print("Duration must be between 0 and 5 seconds")
			return
		if confirm(f"Hold {key!r} for {duration} seconds?"):
			prepare_target()
			pyautogui.keyDown(key)
			try:
				time.sleep(duration)
			finally:
				pyautogui.keyUp(key)
	else:
		print("Unknown operation")


if __name__ == "__main__":
	main()


