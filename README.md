# Free-Hosts-AFK-Earning
A Python script that uses the Selenium library to open a web page and periodically refresh it.

## Requirements

- Python 3.x
- Selenium library
- Chromium based Browser
- Chromedriver

## Installation

1. Ensure that you have Python 3.x installed on your system.
2. Install the Selenium library by running the following command:
   ```python
   pip install selenium
   ```
3. Make sure you have a Chromium based Browser installed on your system.
4. Check your Browser **Chromium** version in your Browser settings or writing [`chrome://version`](chrome://version) in the url.
5. Check for availability and [download](https://googlechromelabs.github.io/chrome-for-testing).

## Config
1. browserLocation = "write/here/your/browser/disk/location".
   _You can find that in `chrome://version` page_.
2. waitingTime = numberOfSeconds.
   _Change according to your need_.
3. hostUrlAfk = "https://urlOfTheHost.com/afk".
   _You must leave `https://` and `/afk - /earn` at the end based on the suffix left by the host_.
4. authorizeLang = "AuthorizeWord".
   _Translate this word according to your language, for example `it: "Autorizza", fr: "Autorise", gr: "Autorisieren", etc.`_.

## Usage

1. Modify the path to the Browser executable in the code. Make sure the path is correct for your Browser installation.
   ```python
   options.binary_location = "C:\\Program Files\\Browser\\Browser\\Application\\browser.exe"
   ```  
2. Run the Python script using the following command:
   ```python
   python afk.py
   ```
3. Login in discord with your account (I recommend using the QR from mobile device).
4. The script will automatically refresh the page every ... minutes and attempt to log in if necessary. (You can change the time according to your preference)


## Disclaimer

Please note that the use of this script may violate the terms of service of Discord or other web services, depending on how it is used. Make sure to use this script in compliance with the guidelines and regulations of the application and services involved.

The use of this script may violate the terms of service of Discord or other web services. Before using the script, make sure to obtain appropriate authorization from the service provider or consult guidelines on web scraping or access automation.

## Contributions

Contributions to this project are welcome. You can open an issue or submit a pull request to suggest improvements or fixes.

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT).

Please refer to the LICENSE file for more information.
