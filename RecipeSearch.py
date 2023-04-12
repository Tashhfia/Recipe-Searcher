from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path="E:\Misc\SeleniumDrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com/")