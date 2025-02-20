import streamlit as st
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode for server deployment
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--no-sandbox')
    return webdriver.Chrome(options=chrome_options)

def scrape_jobs(search_query):
    driver = setup_driver()
    jobs = []
    
    try:
        driver.get("https://www.freelancer.com/jobs")
        
        # Wait for search box
        wait = WebDriverWait(driver, 20)
        search = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@type='search']")
        ))
        
        # Perform search
        search.send_keys(search_query)
        search.send_keys(Keys.ENTER)
        time.sleep(3)
        
        # Get job listings
        job_elements = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, '//*[@class="JobSearchCard-primary-heading"]/a')
        ))
        
        for job in job_elements:
            jobs.append({
                'title': job.text,
                'link': job.get_attribute('href')
            })
            
    except Exception as e:
        st.error(f"An error occurred: {e}")
    finally:
        driver.quit()
        
    return jobs

# Streamlit UI
st.set_page_config(page_title="Freelancer Job Scraper", page_icon="🔍")
st.title("Freelancer Job Scraper")

# Search input
search_query = st.text_input("Enter job search term:", value="django")

if st.button("Search Jobs"):
    with st.spinner("Searching for jobs..."):
        jobs = scrape_jobs(search_query)
        
        if jobs:
            st.success(f"Found {len(jobs)} jobs!")
            
            # Display jobs in a nice format
            for job in jobs:
                with st.expander(job['title']):
                    st.write(f"**Title:** {job['title']}")
                    st.write(f"**Link:** [{job['link']}]({job['link']})")
        else:
            st.warning("No jobs found. Try a different search term.")