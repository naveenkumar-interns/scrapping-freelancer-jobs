from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome options
chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

chrome_options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the website
    topic = "Translation"
    # driver.get(f"https://pro.fiverr.com/search/gigs?query={topic}")
    # driver.get("https://www.upwork.com/nx/search/jobs/")
    driver.get("https://www.freelancer.com/jobs")

    search = driver.find_element(By.XPATH, "//input[@type='search']")

    # Search for "Python"
    search.send_keys("django")
    time.sleep(3)  
    search.send_keys(Keys.ENTER)
    # search.send_keys(Keys.RETURN)
    

    # # Find the search bar using updated method
    # search = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    a = driver.find_elements(By.XPATH, '//*[@class="JobSearchCard-primary-heading"]/a')

    for i in a:
        name = i.text
        link = i.get_attribute('href')
        print(name, link)

    


except Exception as e:
    print(e)

finally:
    # Close the browser
    driver.quit()
