from webdriver_config import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
import csv
from run_session import session
# END IMPORTS


session()  # LOAD SESSION


# wait until sales page completely opens
while 1:
    try:
        sales_page = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located(
            (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div')))
        break
    except TimeoutException:
        print('Timeout exception occured')
        continue

# ACTUAL DATA SCRAPING AUTOMATION
likes = driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[3]/section/div/div/span/a/span/span').text
date_posted = driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[3]/div[2]/div/a/span/time').text
post_description = driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/span/div/span').text

# SCROLL THE ELEMENT
scrollable_ele = driver.find_element(
    By.CSS_SELECTOR, '.x5yr21d.xw2csxc.x1odjw0f.x1n2onr6')

i = 1
comments = []
while 1:
    driver.execute_script(
        "arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_ele)
    time.sleep(1)
    try:
        comment = driver.find_element(
            By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[{i}]/div[1]/div/div[2]/div[1]/div[1]/div/div[2]').text
        i += 1
        comments.append(comment)
        print(comment)
    except NoSuchElementException:
        try:
            gif_element = driver.find_element(
                By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[{i}]/div/div/div[2]/div[1]/div[1]/div/img')
            i += 1
            continue
        except NoSuchElementException:
            break

number_of_comments = i

with open("output.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["comments"])
    for comment in comments:
        writer.writerow([comment])

time.sleep(10)
