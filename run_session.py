from webdriver_config import driver
from load_cookies import cookies
from login import login_and_store_cookies
import time


def session():
    driver.delete_all_cookies()
    if cookies:
        driver.get("https://www.instagram.com")
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get(
            "https://www.instagram.com/reel/C3tCFIWPWXf/?igsh=dWN3Ynh1MnZwYmJi")

    else:
        login_and_store_cookies()
        time.sleep(2)
        driver.get(
            "https://www.instagram.com/reel/C3tCFIWPWXf/?igsh=dWN3Ynh1MnZwYmJi")
