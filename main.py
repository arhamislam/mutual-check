"""
Author: Arham Islam
Date Created: May 23, 2025
Description: Loads Instagram credentials from a .env file, automates Instagram, and compares followers and following lists to identify non-mutual connections.
"""

import os
import logging
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

def load_credentials():
    """Load Instagram credentials from .env file"""
    # Load .env contents and assign to variables
    load_dotenv()
    username = os.getenv("INSTAGRAM_USERNAME")
    password = os.getenv("INSTAGRAM_PASSWORD")

    if not username or not password:
        raise ValueError("Missing Instagram credentials")

    return username, password

def login(driver, username, password):
    driver.get("https://www.instagram.com/")

    driver.implicitly_wait(5)

    usernameInput = driver.find_element(By.NAME, "username")
    passwordInput = driver.find_element(By.NAME, "password")

    usernameInput.send_keys(username)
    passwordInput.send_keys(password)

    loginButton = driver.find_element(By.XPATH, "//button[@type='submit']")
    loginButton.click()

def get_profile(driver, username):
    driver.implicitly_wait(5)

    profile_link = f"//a[starts-with(@href, '/{username}')]"
    profile = driver.find_element(By.XPATH, profile_link)
    profile.click()

    print("here")

def get_followers_list(driver):
    driver.implicitly_wait(5)

    

def main():
    # Create driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = '3'
    logging.getLogger("tensorflow").setLevel(logging.ERROR)

    driver = webdriver.Chrome(options = options)

    # Automation
    try:
        username, password = load_credentials()
        login(driver, username, password)
        get_profile(driver, username)
        get_followers_list(driver)
    
    # Quit
    finally:
        # driver.quit()
        print("END")

if __name__ == "__main__":
    main()
