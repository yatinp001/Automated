

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time

# Environment variables (GitHub Secrets or local override)
USERNAME = os.getenv("USERNAME", "8390216074")  # fallback for local testing
PASSWORD = os.getenv("PASSWORD", "yatin01")

LOGIN_URL = "https://www.hpintfinance.com/index/login/index.html"
EARNINGS_URL = "https://www.hpintfinance.com/index/index/earnings.html"

def run():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Comment this if testing visually
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Step 1: Go to login page
        driver.get(LOGIN_URL)
        time.sleep(2)

        # Step 2: Fill login form
        driver.find_element(By.ID, "phone").send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.CLASS_NAME, "login").click()
        time.sleep(3)

        # Step 3: Navigate to earnings page
        driver.get(EARNINGS_URL)
        time.sleep(3)

        # Step 4: Click "Get it now" button if present
        try:
            button = driver.find_element(By.ID, "btna1")
            button.click()
            print("✅ Clicked 'Get it now' button successfully.")
        except:
            print("⚠️ Button not found — maybe already clicked or hidden.")

        time.sleep(2)

    finally:
        driver.quit()

if __name__ == "__main__":
    run()

