import time
from selenium import webdriver

def refresh_page(url):
    
    options = webdriver.ChromeOptions()
    options.binary_location = "C:\\Program Files\\BrowserSoftware\\Browser\\Application\\browser.exe"

    # Start the browser
    driver = webdriver.Chrome(options=options)

    # Open the web page
    driver.get(url)

    # Initialize number of refresh
    refresh_count = 0


    print("You have 5 minutes to login in discord.")
    time.sleep(300)
    if "https://discord.com/login" in driver.current_url:
        exit()

    while True:
        # Add +1 to refresh number
        refresh_count += 1

        # Check if you need to click the Authorize button on the discord screen, often in the afk pages of free hosts opens the discord page
        if "discord.com/oauth2/authorize" in driver.current_url:
            
            # You maybe need to change 'Authorize' to the consideration of your language
            login_button = driver.find_element_by_xpath("//button[contains(text(), 'Authorize')]") 
  
            login_button.click()

        # Refresh page to avoid afk errors
        driver.refresh()

        # Print when refresh happens
        print(f"Refresh #{refresh_count}")

        # Wait ... time to refreshing
        time.sleep(420)

# Link of the host
refresh_page("https://host.com/afk")
