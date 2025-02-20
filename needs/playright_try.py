import random
import time
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth

def human_like_scroll(page):
    """Simulate human-like scrolling behavior."""
    for _ in range(random.randint(3, 6)):
        scroll_amount = random.randint(200, 500)
        page.mouse.wheel(0, scroll_amount)
        time.sleep(random.uniform(1, 3))

def human_like_typing(element, text):
    """Simulate human-like typing speed."""
    for char in text:
        element.type(char, delay=random.randint(100, 300))  # Random delay for each keypress
    time.sleep(1)

def fiverr_search():
    with sync_playwright() as p:
        # Launch browser with a randomized window size
        browser = p.chromium.launch(headless=False)  # Keep headless=False for human-like behavior
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            viewport={"width": random.randint(1200, 1600), "height": random.randint(700, 1000)}
        )

        # Enable stealth mode to hide automation
        stealth(context)

        page = context.new_page()
        page.goto("https://pro.fiverr.com/", timeout=60000)

        time.sleep(random.uniform(5, 8))  # Mimic human-like delay before interaction

        # Find the search bar using XPath
        search_box = page.locator("//input[@type='search']")
        search_box.click()
        time.sleep(random.uniform(1, 3))

        # Simulate human-like typing
        human_like_typing(search_box, "Python")

        # Press Enter key
        search_box.press("Enter")

        # Wait for results to load
        time.sleep(random.uniform(5, 10))

        # Simulate scrolling
        human_like_scroll(page)

        # Keep browser open for a few seconds before closing
        time.sleep(5)

        # Close everything
        browser.close()

# Run the Fiverr search automation
fiverr_search()
