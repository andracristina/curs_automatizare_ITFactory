from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com')

#selector by link text
#chrome.find_element(By.LINK_TEXT, 'Buttons').click()

# selector by partial link text
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Enabled').click()


sleep(3)
chrome.quit()