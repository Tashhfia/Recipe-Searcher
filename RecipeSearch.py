from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

recipe = "hummus"

service = Service(executable_path="E:\Misc\SeleniumDrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://www.google.com/")

# disable if default browser is in english
driver.find_element(By.PARTIAL_LINK_TEXT, "English").click()
search = driver.find_element(By.ID, "APjFqb")

search.send_keys(f"Best {recipe} recipe", Keys.ENTER)

elem = driver.find_elements(By.CSS_SELECTOR, "div[class^='YwonT'" )
for e in elem:
    print(e.text)

# but = driver.find_element(By.CLASS_NAME, "dU5Kl")
# but.click()