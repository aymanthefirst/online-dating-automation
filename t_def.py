from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from time import sleep

match = []
leftSwipes = 0
rightSwipes = 0
wordsForImidiateSwipeRightFound = 0
wordsForImidiateSwipeLeftFound = 0


def sendKeys(textToSend):
    print('send keys')
    textBox = driver.find_element(By.TAG_NAME, 'textarea')
    textBox.clear()
    textBox.send_keys(textToSend)
    textBox.send_keys(Keys.ENTER)

def removewordsForImidiateSwipeRight(number):
    driver.get("https://www.tinder.com/")
    for i in range(number):
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#t-841490191 > div:nth-child(1) > div:nth-child(2)')))
        element.click()
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#u-1650273590 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div > div.BdStart.Bdc\(\$c-ds-divider-primary\).Fxg\(0\).Fxs\(0\).Fxb\(1\/3\).Miw\(325px\).Maw\(640px\).D\(n\)--m > div > div.W\(100\%\) > div > button.H\(72px\).Tt\(u\).Lts\(\$ls-m\).StyledButton.Bgi\(\$g-ds-background-brand-gradient\)\:h\:\:b.C\(\#fff\)\:h.Fw\(\$semibold\).BdEnd.Bdc\(\$c-ds-divider-primary\).W\(50\%\).focus-button-style')))
        element.click()
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#u916312630 > div > div > div.W\(100\%\) > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(42px\)--s.Mih\(50px\)--ml.Pos\(r\).Ov\(h\).C\(\#fff\).Bg\(\$c-pink\)\:h\:\:b.Bg\(\$c-pink\)\:f\:\:b.Bg\(\$c-pink\)\:a\:\:b.Trsdu\(\$fast\).Trsp\(\$background\).Bg\(\$g-ds-background-brand-gradient\).button--primary-shadow.StyledButton.Bxsh\(\$bxsh-btn\).Fw\(\$semibold\).focus-button-style.My\(12px\).W\(100\%\).D\(b\).Tt\(c\).Typs\(button-1\)')))
        element.click()


def swipeLeft():
    global leftSwipes
    leftSwipes += 1
    print("swipe left")
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.LEFT)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)


def swipeRight():
    global rightSwipes
    rightSwipes += 1
    print("swipe right")
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.RIGHT)
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
    element.send_keys(Keys.ESCAPE)

def randSwipe():
    print("randomswipe")
    rand = random.randint(1, 4)
    if rand == 1:
        swipeRight()
    else:
        swipeLeft()

def nextPics():
    for x in range(1,5):
        sleep(random.uniform(0.5, 1.5))
        print("next pic")
        clickNextPic()
        print("next pic clicked")

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

def clickNextPic():
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.SPACE)


def printLength():
    print('--------------')
    texts = driver.find_elements(By.CLASS_NAME, 'text')
    print('--------------')
    print(len(texts))
    for x in texts:
        print(x.text)
    return len(texts)

def clickwordsForImidiateSwipeRight():
    print("click wordsForImidiateSwipeRight...")
    driver.find_element(By.XPATH, '//button[contains(text(), "wordsForImidiateSwipeRight")]').click()

def sendMessage():
    messageListItems = driver.find_elements(By.CLASS_NAME, 'text')
    messageListItemsList = ['test1', 'test2']
    for x in messageListItems:
        messageListItemsList.append(x.text.lower())
    if not listContains(['ingles', 'english'], messageListItemsList):
        global message1;
        sendKeys(message1);

def getLIstItems():
        return driver.find_elements(By.CLASS_NAME, 'matchListItem')

def getBodyText():
    return driver.find_element(By.CLASS_NAME, 'recsCardboard__cardsContainer').text

def check_for_keywords():
    global wordsForImidiateSwipeLeftFound
    global wordsForImidiateSwipeRightFound
    print('doing the checks')
    body = getBodyText().lower()
    print(body)
    if any(x in body for x in wordsForImidiateSwipeLeft):
        wordsForImidiateSwipeLeftFound += 1
        print("a midget has been found:")
        swipeLeft()
        return True
    if any(x in body for x in wordsForImidiateSwipeRight):
        print("a giant has been found")
        print(getBodyText())
        swipeRight()
        swipeRight()
        wordsForImidiateSwipeRightFound += 1
        return True
        print('end of checks')

def doTheSwipes(country):
    global wordsForImidiateSwipeLeft
    global wordsForImidiateSwipeRight
    global options
    global driver
    options = Options()
    # options.add_argument("--headless")
    wordsForImidiateSwipeRight = ['word1', 'word2', 'word3']
    wordsForImidiateSwipeLeft = ['word4', 'word5', 'word6']
    options.page_load_strategy = 'normal'
    if (country == 'england'):
        options.add_argument("--user-data-dir=C:\\Users\\aharake\\Desktop\\UserData")
        params = {
            "latitude": 51.51405226810681,
            "longitude": -0.15580270062115645,
            "accuracy": 100
        }
    if (country == 'colombia'):
        options.add_argument("--user-data-dir=C:\\Users\\aharake\\Desktop\\UserData2")
        params = {
            "latitude": 10.994145799242013,
            "longitude": -74.81402179382677,
            "accuracy": 100
        }
    if (country == 'brazil'):
        options.add_argument("--user-data-dir=C:\\Users\\aharake\\Desktop\\UserData3")
        params = {
                    "latitude": -23.5174309907172,
                    "longitude": -46.62646995718746,
                    "accuracy": 100
                }

    if (country == 'moscow'):
        options.add_argument("--user-data-dir=C:\\Users\\aharake\\Desktop\\UserData4")
        params = {
                    "latitude": 10.459069023596275,
                    "longitude": -66.897154923381,
                    "accuracy": 100
                }
    if (country == 'beirut'):
        options.add_argument("--user-data-dir=C:\\Users\\aharake\\Desktop\\UserData5")
        params = {
            "latitude": 16.880720817092644,
            "longitude": -99.86089652959136,
            "accuracy": 100
        }
    print('starting to do the swipes')
    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd("Page.setGeolocationOverride", params)
    driver.get("https://www.tinder.com/")
    while rightSwipes < random.randint(40, 50):
        try:
            print("loop starts")
            print("sleeping.....")
            print(driver.find_element(By.TAG_NAME, 'body').text.lower())
            if "out of likes" in driver.find_element(By.TAG_NAME, 'body').text.lower():
                driver.close()
            swipeRight()
            swipeRight()
            swipeRight()
            sleep(random.uniform(0.0, 3))
            driver.find_element(By.TAG_NAME, 'body').click()
            if (check_for_keywords()): continue
            clickNextPic()
            if (check_for_keywords()): continue
            # nextPics()
            randSwipe()
        except Exception as e:
            print(e)
            driver.refresh()
            sleep(10)
        finally:
            print('left swipes')
            print(leftSwipes)
            print("rightSwipes:")
            print(rightSwipes)
            print("wordsForImidiateSwipeLeft found:")
            print(wordsForImidiateSwipeLeftFound)
            print("wordsForImidiateSwipeRight found:")
            print(wordsForImidiateSwipeRightFound)
    driver.close()

