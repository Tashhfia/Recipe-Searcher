import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Scraper:
    def __init__(self,siteLink):
        self.siteLink = siteLink
        self.service = Service(executable_path="E:\Misc\SeleniumDrivers\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome(service= self.service)

    def linkScraper(self, siteLink):

        """Finds links of all the recipes in the website"""
        if isinstance(siteLink, str):
            self.driver.get(siteLink)
            recipeLinks = []
            pageExists = True
            
            while pageExists:
                try:
                    # to avoid StaleElementReferenceException
                    time.sleep(5)
                    # finds all the links in the page
                    links = self.driver.find_elements(By.XPATH, "//h2/a[@rel]")
                    for link in links:
                        recipeLinks.append(link.get_attribute("href"))

                    # finds the last button from a list of buttons
                    nextPage = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[3]/main/div/div/ul/li[last()]")
                
                    if nextPage.get_attribute("class") != "pagination-next":
                        print("all pages scraped...")
                        pageExists = False
                    else:
                        # if its not the last page, then go to next page
                        nextPage.click()
                except:
                    print("Something went wrong!")
                    self.driver.close()

            print(f"No of links extracted: {len(recipeLinks)}")
            self.driver.close()
            return recipeLinks
        else:
            print("This is not a string..!")
            return None
    
    def getLinks(self):

        """Creates a text file with all the scraped links"""

        link_list = self.linkScraper(site)
        if link_list != None:
            with open('recipe_links.txt', 'w') as f:
                for r in link_list:
                    f.write(f"{r}\n")
            print("Links text file generated....")
        else:
            print("No links to save!")

    def ratingsScraper(self):
        print(self.siteLink[1])
        self.driver.get(self.siteLink[0])
        # for page in linkList:
        #     self.driver.get(page)



def readList(path):
    my_file = open(path, "r")
    content = my_file.read()
    data_into_list = content.split("\n")
    print(len(data_into_list))
    my_file.close()
    return data_into_list


if __name__ == '__main__':

    site = "https://www.recipetineats.com/recipes/"
    # s1 = Scraper(site)
    # s1.getLinks()                    // uncomment only if you lose the links text file
    recipeLinks = readList("recipe_links.txt")
    s2 = Scraper(recipeLinks)
    s2.ratingsScraper()

