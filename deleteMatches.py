from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
import random
from time import sleep

options = Options()
options.add_argument("--user-data-dir=C:\\Users\\aharake\\Desktop\\UserData")
options.page_load_strategy = 'normal'
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

def clickMatches():
    print("click matches...")
    driver.find_element(By.XPATH, '//button[contains(text(), "Matches")]').click()

def clickUnmatch():
    print("click unmatch...")
    driver.find_element(By.XPATH, '//button[contains(text(), "Unmatch")]').click()
    
def comfirm():
    print("comfirm")
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div[2]/button[1]').click()


def getLIstItems():
        return driver.find_elements(By.CLASS_NAME, 'matchListItem')


def goToUrl():
    driver.get("https://www.tinder.com/")
    sleep(5)

def clickThroughEachAndDelete():
    print('click through each and send messages')
    goToUrl()
    sleep(1)
    print("--------------")
    driver.find_elements(By.CLASS_NAME, 'matchListItem')
    length = len(getLIstItems()) - 2
    print("--------------")
    for i in range(0, length):
        clickMatches()
        sleep(1)
        getLIstItems()[2].click()
        sleep(1)
        clickUnmatch()
        comfirm()


# start
clickThroughEachAndDelete()