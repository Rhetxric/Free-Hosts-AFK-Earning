#################################################################################################################
#                                                      IMPORTS                                                  #
#################################################################################################################

import time
from selenium import webdriver


#################################################################################################################
#                                                       CONFIG                                                  #
#################################################################################################################

browserLocation = "C:\\Program Files\\BrowserSoftware\\Browser\\Application\\browser.exe" # Your browser disk location
waitingTime = 420 # 7 minutes, you can change as you like
hostUrlAfk = "https://host.com/afk" # Leave the https:// and the /afk or any suffix that the host uses
authorizeLang = "Authorize" # Translate this to your language (it: "Autorizza", fr: "Autorise", gr: "Autorisieren", etc.)


#################################################################################################################
#                                                      PROGRAM                                                  #
#################################################################################################################

def refresh_page(url): 
    # Browser options
    options = webdriver.ChromeOptions()
    # Browser path
    options.binary_location = browserLocation
    # Start the browser
    driver = webdriver.Chrome(options=options)
    # Open the web page
    driver.get(url)
    # Initialize number of refresh
    refresh_count = 0

    print('''
        ______   ________  __    __        ________                                __                     
        /      \ /        |/  |  /  |      /        |                              /  |                    
        /$$$$$$  |$$$$$$$$/ $$ | /$$/       $$$$$$$$/   ______    ______   _______  $$/  _______    ______  
        $$ |__$$ |$$ |__    $$ |/$$/        $$ |__     /      \  /      \ /       \ /  |/       \  /      \ 
        $$    $$ |$$    |   $$  $$<         $$    |    $$$$$$  |/$$$$$$  |$$$$$$$  |$$ |$$$$$$$  |/$$$$$$  |
        $$$$$$$$ |$$$$$/    $$$$$  \        $$$$$/     /    $$ |$$ |  $$/ $$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |
        $$ |  $$ |$$ |      $$ |$$  \       $$ |_____ /$$$$$$$ |$$ |      $$ |  $$ |$$ |$$ |  $$ |$$ \__$$ |
        $$ |  $$ |$$ |      $$ | $$  |      $$       |$$    $$ |$$ |      $$ |  $$ |$$ |$$ |  $$ |$$    $$ |
        $$/   $$/ $$/       $$/   $$/       $$$$$$$$/  $$$$$$$/ $$/       $$/   $$/ $$/ $$/   $$/  $$$$$$$ |
                                                                                                /  \__$$ |
                                                                                                $$    $$/ 
                                                                                                $$$$$$/   

                                            
                                _            ______     _   _               _      
                                | |           | ___ \   | | | |             (_)     
                                | |__  _   _  | |_/ /___| |_| |__ __  ___ __ _  ___ 
                                | '_ \| | | | |    // _ \ __| '_ \\ \/ / '__| |/ __|
                                | |_) | |_| | | |\ \  __/ |_| | | |>  <| |  | | (__ 
                                |_.__/ \__, | \_| \_\___|\__|_| |_/_/\_\_|  |_|\___|
                                        __/ |                                       
                                       |___/                                        
    ''')

    print("Log in to discord.")
    time.sleep(30)

    while "https://discord.com/login" in driver.current_url:
        time.sleep(3)
        print("Log in to discord.") 

    print("Logged in!")

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
        print(time.strftime(" [%H:%M:%S UTC] ", time.gmtime()) + f"Refreshed {refresh_count} times" )
        # Wait ... time to refreshing
        time.sleep(waitingTime)

# Link of the host
refresh_page(hostUrlAfk)
