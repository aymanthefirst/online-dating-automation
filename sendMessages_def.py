from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

def sendKeys(textToSend):
    print('send keys')
    textBox = driver.find_element(By.TAG_NAME, 'textarea')
    textBox.clear()
    textBox.send_keys(textToSend)
    textBox.send_keys(Keys.ENTER)

def getBodyText():
    return driver.find_element(By.CLASS_NAME, 'recsCardboard__cardsContainer').text

def listContains(List1, List2):
    check = False
    # Iterate in the 1st list
    for m in List1:
        # Iterate in the 2nd list
        for n in List2:
            # if there is a match
            if m in n:
                check = True
                return check
    return check

def printLength():
    print('--------------')
    texts = driver.find_elements(By.CLASS_NAME, 'text')
    print('--------------')
    print(len(texts))
    for x in texts:
        print(x.text)
    return len(texts)

def clickMatches():
    print("click matches...")
    matches_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "Matches")]')))
    matches_button.click()

def sendMessage():
    messageListItems = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'text')))
    messageListItemsList = ['test1', 'test2']
    for x in messageListItems:
        messageListItemsList.append(x.text.lower())
    if not listContains(['ingles', 'english'], messageListItemsList):
        global message1;
        sendKeys(message1)

def getLIstItems():
    return WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'matchListItem')))

def goToUrl():
    driver.get("https://www.tinder.com/")
    sleep(10)


def clickThroughEachSendingMessages(country):
    try:
        global options
        global driver
        global message1
        options = Options()
        options.page_load_strategy = 'normal'
        if (country == 'england'):
            options.add_argument("--user-data-dir=C:\\Users\\aharake\\Desktop\\UserData")
            params = {
                "latitude": 51.51405226810681,
                "longitude": -0.15580270062115645,
                "accuracy": 100
            }
            message1 = "this is the first message"
        if (country == 'colombia'):
            options.add_argument("--user-data-dir=C:\\Users\\aharake\\Desktop\\UserData2")
            params = {
                "latitude": 10.994145799242013,
                "longitude": -74.81402179382677,
                "accuracy": 100
            }
            message1 = "this is the first message"
        if (country == 'brazil'):
            options.add_argument("--user-data-dir=C:\\Users\\aharake\\Desktop\\UserData3")
            params = {
                "latitude": -23.5174309907172,
                "longitude": -46.62646995718746,
                "accuracy": 100
            }
            message1 = "this is the first message"
        if (country == 'moscow'):
            options.add_argument("--user-data-dir=C:\\Users\\aharake\\Desktop\\UserData4")
            params = {
                "latitude": 10.459069023596275,
                "longitude": -66.897154923381,
                "accuracy": 100
            }
            message1 = "this is the first message"
        if (country == 'beirut'):
            options.add_argument("--user-data-dir=C:\\Users\\aharake\\Desktop\\UserData5")
            params = {
                "latitude": 16.880720817092644,
                "longitude": -99.86089652959136,
                "accuracy": 100
            }
            message1 = "this is the first message"
        # options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.execute_cdp_cmd("Page.setGeolocationOverride", params)

        print('click through each and send messages')
        goToUrl()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'matchListItem')))
        length = len(getLIstItems()) - 2
        i = 0
        while len(getLIstItems()) > 1:
            clickMatches()
            wait = WebDriverWait(driver, 10)
            matches = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'matchListItem')))
            matches[-1].click()
            sendMessage()
    except Exception as e:
        print(e)
        # sleep(5)
        # clickThroughEachSendingMessages(country)
    finally:
        driver.close()




 