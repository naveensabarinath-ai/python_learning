# Daily Report Bot

# bot to launch this site   and get the gold price of bangalore and send it to the excel file
#  https://ratestoday.in/gold-price-today/bangalore/

# Output: daily_report_2023-06-01_12-00-00.xlsx stored in the Output folder with the current date and time in the filename

from importlib.resources import path

import pyautogui
import time
import os
import re

import pyperclip
from datetime import datetime
import win32com.client

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.5

pyautogui.hotkey('win', 'r')  # Open the Run dialog
time.sleep(1)  # Wait for the Run dialog to open

pyautogui.write('chrome')  # Type 'chrome' to open Google Chrome
pyautogui.press('enter')  # Press Enter to open Chrome
time.sleep(3)  # Wait for Chrome to open

print("Navigating to the gold price page.")
pyautogui.hotkey('ctrl', 't')  # Open a new tab
pyautogui.typewrite('https://ratestoday.in/gold-price-today/bangalore/')  # Type the URL
pyautogui.press('enter')  # Press Enter to navigate to the URL
time.sleep(3)  # Wait for the page to load

pyperclip.copy('')  # Clear the clipboard
# Copy data
pyautogui.hotkey('ctrl', 'a')  # Select all text
pyautogui.hotkey('ctrl', 'c')  # Copy the selected text
time.sleep(1)  # Wait for the copy operation to complete
pageText = pyperclip.paste()  # Get the copied text

pattern = re.compile(
    r"(?P<gold_type>(?:22K|24K|18K)\s+Gold)\s+"
    r"(?P<purity>\d+)\s+purity.*?"
    r"₹\s*(?P<price>[\d,]+)\s*"
    r"(?P<arrow>[▼▲])\s*₹?\s*(?P<change>[\d,]+)",
    re.IGNORECASE | re.DOTALL,
)

gold_rates = tuple(
    (
        match["gold_type"],
        int(match["purity"]),
        int(match["price"].replace(",", "")),
        "decreased" if match["arrow"] == "▼" else "increased",
        int(match["change"].replace(",", "")),
    )
    for match in pattern.finditer(pageText)
)

if not gold_rates:
    raise ValueError("No gold-rate information found in the copied text.")

print(gold_rates)

#Close the Chrome browser
pyautogui.hotkey('alt', 'f4')  # Close the current window

#Open Excel and write the data
pyautogui.hotkey('win', 'r')  # Open the Run dialog

pyautogui.write('excel')  # Type 'excel' to open Excel
pyautogui.press('enter')  # Press Enter to open Excel
time.sleep(3)  # Wait for Excel to open

pyautogui.hotkey('ctrl', 'n')  # Open a new workbook

#Add the current date and time to the first row
current_datetime = datetime.now().strftime("%Y-%m-%d")
pyautogui.write(f"Gold Rates Report - {current_datetime}")  # Write the current date and time
pyautogui.press('enter')  # Move to the next row

# Write the header row
pyautogui.write('Gold Type\tPurity\tPrice\tChange Direction\tChange Amount')  # Write the header row
pyautogui.press('enter')  # Move to the next row

# Iterate through the gold rates and write them to the Excel sheet
for gold_type, purity, price, change_direction, change_amount in gold_rates:
    pyautogui.write(f"{gold_type}\t{purity}\t{price}\t{change_direction}\t{change_amount}")
    pyautogui.press('enter')  # Move to the next row

excel = win32com.client.GetActiveObject("Excel.Application")
worksheet = excel.ActiveWorkbook.ActiveSheet

report_range = worksheet.Range("A1:E5")
report_range.Borders.LineStyle = 1  # Continuous borders
report_range.Borders.Weight = 2     # Thin borders

worksheet.Range("A1:E2").Font.Bold = True
worksheet.Range("A1:E1").Interior.Color = 65535       # Yellow
worksheet.Range("A2:E2").Interior.Color = 0x50B000   # Green


workbook = excel.ActiveWorkbook
worksheet.Name = "Gold Rates"
#get the current directory

#Append the folder Output path to the current directory
output_dir = os.path.dirname(os.path.abspath(__file__))+"/Output"


file_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_path = os.path.join(
    output_dir,
    f"daily_report_{file_timestamp}.xlsx",
)

workbook.SaveAs(Filename=file_path, FileFormat=51)

print(f"Workbook saved to: {file_path}")


#Take a screenshot of the Excel sheet
# Save a screenshot of the screen, including the Excel report
snapshot_path = os.path.join(
    output_dir,
    f"daily_report_{file_timestamp}.png",
)
pyautogui.screenshot().save(snapshot_path)

print(f"Snapshot saved to: {snapshot_path}")


# Close current window (Excel)
pyautogui.hotkey('alt', 'f4')  # Close the current window





