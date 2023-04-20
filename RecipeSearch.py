import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import pickle

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
                    pageExists = False

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

        """ Takes a list of links and returns a dictionary with all scraped recipe names, 
        ratings, votes and course."""
        
        rev = {"Name":[], "Rating": [], "Votes": [], "Course": []}

        for page in self.siteLink:
            
            try:
                self.driver.get(page)
                time.sleep(5)
                recipe = self.driver.find_element(By.XPATH, 
                                                "/html/body/div[1]/div[3]/div[2]/main/article/header/div[2]/div/a")
                print(recipe.text)
                # if its a recipe then proceed
                if recipe.text == "RECIPE V":
                    recipe.click()
                    time.sleep(8)
                    name = self.driver.find_element(
                        By.XPATH,"/html/body/div[1]/div[3]/div[2]/main/article/div/div[4]/div/div[2]/div[1]/h2").text
                    rating = self.driver.find_element(
                        By.XPATH,"/html/body/div[1]/div[3]/div[2]/main/article/div/div[4]/div/div[2]/div[1]/div[3]/div/span[1]").text
                    votes = self.driver.find_element(
                        By.XPATH,"/html/body/div[1]/div[3]/div[2]/main/article/div/div[4]/div/div[2]/div[1]/div[3]/div/span[2]").text
                    course = self.driver.find_element(
                        By.XPATH,"/html/body/div[1]/div[3]/div[2]/main/article/div/div[4]/div/div[2]/div[1]/div[2]/div[last()-1]/span[2]").text
                    
                    # if element wasnt found, append null
                    if name:
                        rev["Name"].append(name)
                    else:
                        rev["Name"].append("Null")
                    if rating:    
                        rev["Rating"].append(rating)
                    else:
                        rev["Rating"].append("Null")
                    if votes:
                        rev["Votes"].append(votes)
                    else:
                        rev["Votes"].append("Null")
                    if course:
                        rev["Course"].append(course)
                    else:
                        rev["Course"].append("Null")
                    
                    print(rev)

                # otherwise skip entry
                else:
                    print("this is not a recipe!")
                    continue
            except:
                print("Element not found")
                # return rev

        self.driver.close()

        return rev

def readList(path):

    """ Finds and opens text file and converts it to a list"""

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
    recipe_dict = s2.ratingsScraper()

    # keep either the pickle or csv codes
    # Store data (serialize)
    try:
        with open('recipe_dict.pickle', 'wb') as handle:
            pickle.dump(recipe_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    except:
        print("error while pickling!")
    try:
        df = pd.DataFrame.from_dict(recipe_dict) 
        df.to_csv('recipe_info.csv')
    except:
        print("error while saving to csv")

    # # Load data (deserialize)
    # with open('filename.pickle', 'rb') as handle:
    #     unserialized_data = pickle.load(handle)

    # print(your_data == unserialized_data)

    

