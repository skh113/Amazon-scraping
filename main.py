from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Initializing variables
url = "https://www.amazon.com/s?k=gaming+laptop&ref=nb_sb_noss"
sleep_time = 3

# Set up the webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
sleep(sleep_time)

# get the search results
search_results = driver.find_element(By.CLASS_NAME, "s-search-results")
laptop_titles = search_results.find_elements(By.TAG_NAME, "h2")
laptop_prices = search_results.find_elements(By.CLASS_NAME, "a-price-whole")
laptop_rate = search_results.find_elements(By.CLASS_NAME, "a-icon-alt")

laptops = []
for item in laptop_titles:
    print(item.text)
for item in laptop_prices:
    print(item.text)
for item in laptop_rate:
    print(item.text)

# Close the webdriver
driver.quit()
