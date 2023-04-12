from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Disabling images
# TODO: disable css as well
options = Options()
options.headless = True

chrome_options = webdriver.ChromeOptions()
# this will disable image loading
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
# or alternatively we can set direct preference:
chrome_options.add_experimental_option(
    "prefs", {"profile.managed_default_content_settings.images": 2}
)

# Initializing variables
url = "https://www.amazon.com/s?k=gaming+laptop&ref=nb_sb_noss"
sleep_time = 3
next_page = "s-pagination-next"
last_url = ""

# Set up the webdriver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options, chrome_options=chrome_options)
driver.get(url)
sleep(sleep_time)

# We go through pages of search result
try:
    with open("product_links.txt", "w") as file:
        while driver.find_element(By.CLASS_NAME, next_page):
            # checking if it's the last page of search results
            if last_url == driver.current_url:
                break

            search_results = driver.find_element(By.CLASS_NAME, "s-search-results")
            for item in search_results.find_elements(By.CLASS_NAME, "s-no-outline"):
                print(item.get_attribute("href"), file=file)

            # Going to next page
            last_url = driver.current_url
            driver.find_element(By.CLASS_NAME, next_page).click()
            sleep(sleep_time)
except (EOFError, IOError) as err:
    print(err)

# Close the webdriver
# driver.quit()
