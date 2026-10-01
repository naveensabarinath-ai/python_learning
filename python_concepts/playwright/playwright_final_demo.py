import playwright


from playwright.sync_api import sync_playwright
from datetime import datetime

print("Playwright version:", playwright.__version__)
print("Python version:", playwright.__version__)

#Daily weather report bot 
#Chromium --> Weather Site --> Search for city --> Click on city --> Extract weather info --> Print to console

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://weather.com/")
    page.wait_for_load_state("networkidle")
    
    # Search for city
    search_box = page.locator("input[name='search']")
    search_box.fill("New York")
    search_box.press("Enter")
    
    # Wait for the results to load and click on the first result
    page.wait_for_selector("a[href*='/weather/today/']")
    first_result = page.locator("a[href*='/weather/today/']").first
    first_result.click()
    
    # Extract weather information
    page.wait_for_selector("span[data-testid='TemperatureValue']")
    temperature = page.locator("span[data-testid='TemperatureValue']").inner_text()
    condition = page.locator("div[data-testid='wxPhrase']").inner_text()
    
    # Print to console
    print(f"Current weather in New York: {temperature}, {condition}")
    
    browser.close()