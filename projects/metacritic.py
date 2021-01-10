from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/Dell/Downloads/chromedriver")

url = "https://www.metacritic.com/game"
driver.get(url)
time.sleep(3)
driver.quit()
