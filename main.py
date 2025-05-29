"""
Author: Arham Islam
Date Created: May 23, 2025
Description: Loads Instagram credentials from a .env file, automates Instagram, and compares followers and following lists to identify non-mutual connections.
"""

import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    driver.get("https://www.instagram.com/")

    driver.implicitly_wait(1)

    u = driver.find_element(By.NAME, "username")
    p = driver.find_element(By.NAME, "password")

    u.send_keys(username)
    p.send_keys(password)

    l = driver.find_element(By.XPATH, "//button[@type='submit']")
    l.click()

def main():
    # Load .env contents and assign to variables
    load_dotenv()
    username = os.getenv("INSTAGRAM_USERNAME")
    password = os.getenv("INSTAGRAM_PASSWORD")

    # Create driver
    driver = webdriver.Chrome()

    # Automation
    try:
        login(driver, username, password)
    
    # Quit
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
