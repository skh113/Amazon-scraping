from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Initializing variables
url = "https://www.amazon.com/s?k=gaming+laptop&ref=nb_sb_noss"
sleep_time = 3
next_page = "s-pagination-next"
last_url = ""

# Set up the webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
sleep(sleep_time)

try:
    while driver.find_element(By.CLASS_NAME, next_page):
        if last_url == driver.current_url:
            break

        temp = driver.find_element(By.CLASS_NAME, next_page)
        print(driver.current_url)
        last_url = driver.current_url
        temp.click()
        sleep(sleep_time)
except:
    print("finish or not found")


# Close the webdriver
driver.quit()
