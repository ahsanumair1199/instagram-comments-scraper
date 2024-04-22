from webdriver_config import driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pickle
import time
import insta_secrets
from webdriver_config import driver
# END IMPORTS


def login_and_store_cookies():
    driver.get(
        "https://www.instagram.com/accounts/login/?next=%2Flogin%2F&source=desktop_nav")
    while 1:
        try:
            driver.find_element(
                By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys(insta_secrets.INSTA_EMAIL)
            driver.find_element(
                By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys(insta_secrets.INSTA_PASSWORD)
            driver.find_element(
                By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]').click()
            break
        except NoSuchElementException:
            continue

    # Get cookies
    time.sleep(3)
    cookies = driver.get_cookies()
    with open("instagram_cookies.pkl", "wb") as cookies_file:
        pickle.dump(cookies, cookies_file)
