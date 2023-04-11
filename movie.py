from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Initializing variables
url = "https://subslikescript.com/movies"
sleep_time = 3

# initialize webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# navigate to the website
driver.get(url)
sleep(sleep_time)

# find the ul element with scripts-list class
scripts_list = driver.find_element(By.CLASS_NAME, "scripts-list")

# find all the "a" tags in the ul element and print their text
for a_tag in scripts_list.find_elements(By.TAG_NAME, "a"):
    print(a_tag.text)

# close the webdriver
driver.quit()
