import  pyautogui
import  time
from datetime import datetime
import pyperclip

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

print("1. Opening the chrome browser and navigating to the specified URL...")
time.sleep(2)  # Wait for 2 seconds before starting the automation

pyautogui.hotkey('win', 'r')  # Open the Run dialog
time.sleep(1)  # Wait for the Run dialog to open    
pyautogui.write('chrome')  # Type 'chrome' to open Google Chrome
pyautogui.press('enter')  # Press Enter to open Chrome
time.sleep(3)  # Wait for Chrome to open


print("2. Navigating to new tab.")
pyautogui.hotkey('ctrl', 't')  # Open a new tab
time.sleep(1)  # Wait for the new tab to open

pyautogui.typewrite('https://www.accuweather.com/en/in/bengaluru/204108/weather-forecast/204108#google_vignette')  # Type the URL
pyautogui.press('enter') 

time.sleep(3) 

# Copy data
pyautogui.hotkey('ctrl', 'a')  # Select all text
time.sleep(1)  # Wait for the selection to complete
pyautogui.hotkey('ctrl', 'c')  # Copy the selected text

copied_text = pyperclip.paste()

# write the copied data to a text file
with open('weather_data.txt', 'w', encoding='utf-8') as file:
    file.write(f"Weather data copied on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    file.write(copied_text)  # Write the copied text to the file  
