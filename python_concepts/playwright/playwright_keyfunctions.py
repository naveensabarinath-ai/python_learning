from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    try:
        url = "https://www.accuweather.com/en/in/bengaluru/204108/weather-forecast/204108"

        page.goto(url)

        page.screenshot(path="accuweather.png")


        page.click("text=AIR QUALITY")
        page.screenshot(path="accuweather_airquality.png")

        #typing into the search box
        search_box = page.locator("input[placeholder='Search for a city or zip code']")
        search_box.fill("Bengaluru")
        search_box.press("Enter")

        #Wait for the search results to load and click on the first result
        page.wait_for_selector("text=Bengaluru, Karnataka, India")
        page.click("text=Bengaluru, Karnataka, India")

        #Extract the air quality information
        air_quality_info = page.locator("div.air-quality-info").inner_text()

        #Print the air quality information
        print("Air Quality Information for Bengaluru:")
        print(air_quality_info)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        browser.close()
    