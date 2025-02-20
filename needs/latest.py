
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 20)

try:
    # Open the website
    driver.get("https://www.freelancer.com/jobs")
    
    # Wait for search box and interact with it
    search = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='search']")))
    search.send_keys("django")
    search.send_keys(Keys.ENTER)

    # Wait for the search results to load and stabilize
    time.sleep(3)  # Allow time for results to load
    
    # Wait for job cards and extract information
    job_links = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, '//*[@class="JobSearchCard-primary-heading"]/a')
    ))

    # Extract information from each job card
    for job in job_links:
        try:
            name = job.text
            link = job.get_attribute('href')
            print(f"Job Title: {name}")
            print(f"Link: {link}\n")
        except Exception as e:
            print(f"Error processing job: {e}")
            continue

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()