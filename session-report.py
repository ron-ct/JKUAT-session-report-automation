import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options


# Load environment variables from .env file
load_dotenv()

# Retrieve credentials from .env
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# Helper function to simulate human-like typing
def human_typing(element, text, min_delay=0.1, max_delay=0.4):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(min_delay, max_delay))

# Helper function to mimic human delays
def human_delay(min_seconds=1.0, max_seconds=3.0):
    time.sleep(random.uniform(min_seconds, max_seconds))

service = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " 
                            "(KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open Google and mimic a slight delay
    driver.get("https://www.google.com")
    human_delay(2, 4)

    # Optional: Accept cookies if prompted (adjust selector if necessary)
    try:
        accept_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='I agree']"))
        )
        human_delay(1, 2)
        accept_button.click()
    except Exception:
        pass  # Continue if there's no cookie prompt

    # Locate the search box
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    human_delay(1, 2)
    
    # Mimic human typing for the search term
    human_typing(search_box, "jkuat students portal", 0.15, 0.3)
    human_delay(0.5, 1)
    search_box.send_keys(Keys.RETURN)

    # Wait for search results to load and then mimic a pause before clicking
    #had to add more time so that I can manualy solve the captchas
    first_result = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "(//h3)[1]"))
    )
    human_delay(2, 4)
    first_result.click()

    # Wait for the portal page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    human_delay(2, 4)

    # --- Sign In Section ---
    # Replace the selectors with the actual ones from your sign in page
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "exampleFormControlInput1"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    human_delay(1, 2)

    # Simulate typing for username and password
    human_typing(username_field, USERNAME, 0.15, 0.3)
    human_delay(0.5, 1)
    human_typing(password_field, PASSWORD, 0.15, 0.3)
    human_delay(1, 2)

    sign_in_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign In']")))


    human_delay(1, 2)
    sign_in_button.click()

    # --- Navigation to Session Report ---
    # Wait for the dashboard to load then click the session report tab
    # Wait until the "Admission" menu is clickable
    admission_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "admission")))

    # Click the child anchor (dropdown toggle) within the Admission menu
    admission_toggle = admission_menu.find_element(By.CSS_SELECTOR, "a.menu_sub")
    admission_toggle.click()

    # Optional: wait a moment for the dropdown animation to complete
    time.sleep(1)

    # Now wait for the "Reporting" link to be clickable and click it
    reporting_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "reporting")))
    reporting_link.click()

    report_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.primary-btn.mb-2")))

    # Click the "Report" button.
    report_button.click()

    # Give the page some extra time to update
    human_delay(5, 7)

    # --- Take Screenshot ---
    screenshot_path = os.path.join(os.path.expanduser("~"), "Pictures", "session_report.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")

finally:
    driver.quit()
