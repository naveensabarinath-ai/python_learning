import os

from playwright.sync_api import sync_playwright
from datetime import datetime

# Need to open cricbuzz.com and extract the live score of the ongoing match or recent match. The extracted score should be printed to the console. and take the screenshot of the score and paste it..
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.cricbuzz.com/")
    page.wait_for_load_state("networkidle")
    
    # Click on the live score section
    page.click("text=Live Scores")
    
    page.wait_for_load_state("networkidle")

    #Append the folder Output path to the current directory
    output_dir = os.path.dirname(os.path.abspath(__file__))+"/Output"
    
    page.screenshot(path=f"{output_dir}/cricbuzz_score_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png") 
    
    browser.close()
