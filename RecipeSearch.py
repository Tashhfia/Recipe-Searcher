import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Scraper:
    

    def __init__(self,site):
        self.site = site
        self.service = Service(executable_path="E:\Misc\SeleniumDrivers\chromedriver_win32\chromedriver.exe")

    def linkScraper(self, site):

        """Finds links of all the recipes in the website"""
        driver = webdriver.Chrome(service= self.service)
        driver.get(site)
        recipeLinks = []
        pageExists = True
        
        while pageExists:
            try:
                # to avoid StaleElementReferenceException
                time.sleep(5)
                # finds all the links in the page
                links = driver.find_elements(By.XPATH, "//h2/a[@rel]")
                for link in links:
                    recipeLinks.append(link.get_attribute("href"))

                # finds the last button from a list of buttons
                nextPage = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[3]/main/div/div/ul/li[last()]")
            
                if nextPage.get_attribute("class") != "pagination-next":
                    print("all pages scraped...")
                    pageExists = False
                else:
                    # if its not the last page, then go to next page
                    nextPage.click()
            except:
                print("Something went wrong!")
                driver.close()

        print(f"No of links extracted: {len(recipeLinks)}")
        driver.close()
        return recipeLinks
    
    def get_links(self):
        link_list = self.linkScraper(site)
        with open('recipe_links.txt', 'w') as f:
            for r in link_list:
                f.write(f"{r}\n")

# uncommnent only if you lose the links



if __name__ == '__main__':

    site = "https://www.recipetineats.com/recipes/"
    s1 = Scraper(site)
    # s1.get_links()                    // uncomment only if you lose the links text file
    

    
    print("after __name__ guard")
