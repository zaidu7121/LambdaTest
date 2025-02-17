import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service 
import time


# Fixture to initialize and quit WebDriver
@pytest.fixture
def driver():
    service = Service(r"C:\Users\DEll\Desktop\selenium_test_project\Drivers\geckodriver.exe")
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()


# Test Case: Validate Search Functionality
def test_search_new_york(driver):
    # Step 1: Navigate to Selenium Playground Table Search Demo
    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
    driver.maximize_window()
    time.sleep(2)

    # Step 2: Locate and Interact with Search Box
    search_box = driver.find_element(By.XPATH, "//input[@type='search']")
    search_box.send_keys("New York")
    time.sleep(2)

    # Step 3: Validate Search Results
    rows = driver.find_elements(By.XPATH, "//table[@id='example']//tbody//tr")
    visible_rows = [row for row in rows if row.is_displayed()]

    # Assert to ensure 5 entries are displayed
    assert len(visible_rows) == 5, f"Expected 5 entries, but found {len(visible_rows)}"
