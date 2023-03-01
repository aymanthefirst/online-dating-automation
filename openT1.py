from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--user-data-dir=C:\\Users\\aharake\\Desktop\\UserData1")
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
params = {
    "latitude": 51.51405226810681,
    "longitude": -0.15580270062115645,
    "accuracy": 100
}
driver.execute_cdp_cmd("Page.setGeolocationOverride", params)


def clickMessages():
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "Messages")]')))
    element.click()





driver.get("https://www.tinder.com/")
sleep(5)
clickMessages()




