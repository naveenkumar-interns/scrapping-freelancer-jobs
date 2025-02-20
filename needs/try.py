import time
import random
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Configure Chrome options with additional settings
chrome_options = uc.ChromeOptions()

# Add existing stealth settings
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--no-first-run")
chrome_options.add_argument("--no-service-autorun")
chrome_options.add_argument("--no-default-browser-check")
chrome_options.add_argument("--disable-popup-blocking")

# Add these new arguments to handle network errors
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--dns-prefetch-disable")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--allow-running-insecure-content")

# Update user agent to latest Chrome version
chrome_options.add_argument(f"--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36")

# Initialize undetected chromedriver with updated version
driver = uc.Chrome(
    options=chrome_options,
    headless=False,
    version_main=132  # Update this to match your Chrome version (132)
)

# Execute CDP commands to hide automation
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
    });
    """
})

try:
    # Human-like delay before actions
    def human_delay(min=1, max=3):
        time.sleep(random.uniform(min, max))

    # Open website with randomized delays
    driver.get("https://www.freelancer.com/jobs/?keyword=django")
    human_delay(5, 8)  # Longer initial delay

    # Wait for page elements with randomized patterns
    search = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
    )

    # Human-like typing simulation
    for char in "Python":
        search.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))
    
    # Add random mouse movements
    action = webdriver.ActionChains(driver)
    action.move_to_element_with_offset(search, random.randint(-5, 5), random.randint(-5, 5))
    action.perform()
    
    human_delay(0.5, 1.5)
    search.send_keys(Keys.RETURN)

    # Add random scrolling
    driver.execute_script(f"window.scrollBy(0, {random.randint(50, 200)})")
    human_delay(2, 4)

finally:
    # Add cleanup delay
    time.sleep(random.uniform(2, 5))
    driver.quit()