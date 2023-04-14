import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup

recipe = "hummus"

service = Service(executable_path="E:\Misc\SeleniumDrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://www.recipetineats.com/recipes/")

def find_links():
    recipeLinks = []
    pageExists = True
    while pageExists:
        # to avoid StaleElementReferenceException
        time.sleep(5)
        links = driver.find_elements(By.XPATH, "//h2/a[@rel]")
        for link in links:
            recipeLinks.append(link.get_attribute("href"))

        nextPage = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[3]/main/div/div/ul/li[last()]")
    
        if nextPage.get_attribute("class") != "pagination-next":
            print("all pages scraped...")
            pageExists = False
        else:
            nextPage.click()

    print(len(recipeLinks))
    return recipeLinks

# driver.find_element(By.CLASS_NAME, "general-search__icon-button").click()
# search = driver.find_element(By.CLASS_NAME, 'general-search__input')

# search.click()
# time.sleep(5)
# #driver.find_element(By.ID, 'fullscreen-nav__search__search-input').send_keys(f"Best {recipe} recipe", Keys.ENTER)
# driver.find_element(By.XPATH, "/html/body/header/div[2]/nav/div[1]/form/div/input").send_keys(f"Best {recipe} recipe", Keys.ENTER)

#search.send_keys(f"Best {recipe} recipe", Keys.ENTER)

# driver.find_element(By.CSS_SELECTOR, "div[aria-label ^= 'Show more']").click()

# try:
#     # elem = driver.find_elements(By.CSS_SELECTOR, "div[class^='YwonT'" )
#     elem = driver.find_elements(By.CSS_SELECTOR, 'div[id = "isl_1-1"]')

#     for k in elem:
#         print(k.text)
#     print("-----------------------")
#     # for c in t:
#     #     print(c.text)


# except Exception as e:
#     print("Element not found...!")
#     print(e) 




# but = 
# but.click()