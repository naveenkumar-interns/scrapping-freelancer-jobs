# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status




@api_view(["GET"])
def home(request):
    data = {"staus": "working"}
    return Response(data, status=status.HTTP_200_OK)




import time
import pandas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # Run in headless mode for server deployment
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--no-sandbox')
    return webdriver.Chrome(options=chrome_options)

def freelancer_scrapper(search_query):
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
            df = pandas.DataFrame(jobs)
            df.to_csv('jobs.csv')

            
    except Exception as e:
        raise(f"An error occurred: {e}")
    finally:
        driver.quit()
        
    return jobs

def upwork_scrapper(search_query):
    driver = setup_driver()
    jobs = []
    try:
        driver.get("https://www.upwork.com/")
        
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
            (By.XPATH, '//*[@class="job-title-link break visited"]')
        ))
        
        for job in job_elements:
            jobs.append({
                'title': job.text,
                'link': job.get_attribute('href')
            })
            df = pandas.DataFrame(jobs)
            df.to_csv('jobs.csv')

            
    except Exception as e:
        raise(f"An error occurred: {e}")
    finally:
        driver.quit()

    return jobs

def fiverr_scrapper(search_query):
    driver = setup_driver()
    jobs = []
    try:
        driver.get("https://www.fiverr.com/")
        
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
            (By.XPATH, '//*[@class="gig-link-main"]')
        ))
        
        for job in job_elements:
            jobs.append({
                'title': job.text,
                'link': job.get_attribute('href')
            })
            df = pandas.DataFrame(jobs)
            df.to_csv('jobs.csv')

            
    except Exception as e:
        raise(f"An error occurred: {e}")
    finally:
        driver.quit()

    return jobs

#routes


@api_view(["GET"])
def scrape_jobs(request):
    search_query = request.GET.get("search_query","")
    platform = request.GET.get("platform","")

    print(search_query, platform)

    if platform == "freelancer.com":
        jobs = freelancer_scrapper(search_query)
    elif platform == "upwork.com":
        jobs = upwork_scrapper(search_query)
    elif platform == "fiverr.com":
        jobs = fiverr_scrapper(search_query)
    else:
        jobs = []

    

    return Response(jobs, status=status.HTTP_200_OK)




