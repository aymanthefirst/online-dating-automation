Online Dating Automation
=====================================================

This project is a script that automates swiping left and right on the Tinder dating app, as well as sending the first message to any matches. The automation uses Python Selenium and AutoHotkey scripts, and allows for multiple Tinder accounts to be linked and run simultaneously. The user can also choose their location, and the script sets the geolocation accordingly. Additionally, the script takes in a list of words to avoid, and swipes left if it comes across any of them, and swipes right for good words.

Requirements
------------

-   Python 3.7 or higher
-   Selenium Python library
-   AutoHotkey
-   ChromeDriver

Setup
-----

1.  Clone the repository to your local machine.
2.  Install the required Python libraries by running `pip install -r requirements.txt` in your terminal.
3.  Download and install AutoHotkey from the official website.
4.  Download the ChromeDriver executable and add it to your PATH variable.
5.  Open `config.py` and add your Tinder account credentials, as well as any words to avoid and good words.
6.  Run the script using `python tinder_auto.py`.

Usage
-----

The script will prompt you to enter your location. Enter your location in the format `City, State, Country` and press enter.

The script will then open a Chrome window and log into your Tinder account. It will swipe left or right based on the words in your `config.py` file.

If the script comes across a match, it will send the first message based on the message in the `config.py` file.

The script can be run multiple times with different account credentials by adding the credentials to the `config.py` file and running the script again.

Disclaimer
----------

This script is intended for educational purposes only. Use at your own risk. The developers are not responsible for any actions taken using this script.
