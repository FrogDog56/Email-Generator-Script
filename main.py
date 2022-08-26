import numbers
import time
import random
import string
import os, sys
import warnings
import time, requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

url = 'https://proton.me/pricing'
length = 8

def gen():
    file = open("accounts.txt", "a")

    warnings.filterwarnings("ignore", category=DeprecationWarning) 

    option = webdriver.ChromeOptions()
    option.add_argument("--mute-audio")
    option.add_extension(os.getcwd() + '\solver.crx') # gets the directory of the hCap solver.
    option.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(ChromeDriverManager().install(), options = option)
    driver.get(url)

    driver.find_element(By.XPATH, "//*[@id='gatsby-focus-wrapper']/main/div/div[1]/div[1]/div/div[3]/div[1]/div/div[2]/a").click()

    time.sleep(1.5)

    element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/iframe")
    driver.switch_to.frame(element)
    letters = string.ascii_lowercase
    nums = string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    result_str = result_str + random.choice(nums)
    driver.find_element(By.XPATH, "//*[@id='email']").send_keys(result_str)
    file.write("\n email: " + result_str +"@proton.me\n")
    file.write("username: " + result_str + "\n")
    driver.switch_to.default_content()

    time.sleep(2)

    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))

    driver.find_element(By.XPATH, "//*[@id='password']").send_keys(result_str + "!")

    driver.find_element(By.XPATH, "//*[@id='repeat-password']").send_keys(result_str + "!")
    file.write("password: " + result_str + "!")
    file.close()

    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/button").click()

    time.sleep(4)

    try:
        element = driver.find_element(By.XPATH, "//*[@id='key_0']/iframe")
        driver.switch_to.frame(element)
        driver.find_element(By.XPATH, "//*[@id='html_element']/iframe").click()
        driver.switch_to.default_content()
    except Exception:
        #driver.find_element(By.XPATH, "//*[@id='email']").send_keys(code_email)
        #driver.find_element(By.XPATH, "//*[@id='key_0']/button").click()
        #driver.execute_script("window.open('');")
        #driver.switch_to.window(driver.window_handles[1])
        #driver.get("https://proton.me/")
        #time.sleep(4)
        #driver.find_element(By.XPATH, "//*[@id='gatsby-focus-wrapper']/header/div/div[3]/a[1]").click()
        #time.sleep(2)
        #driver.find_element(By.XPATH, "//*[@id='username']").send_keys(code_email)
        #driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)
        #time.sleep(2)
        #driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/button").click()
        #time.sleep(10)
        pass

    time.sleep(100)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/main/div[2]/form/button").click()

    time.sleep(10)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/main/div[2]/form/button[2]").click()

    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[4]/dialog/div/div[3]/button[1]").click()

for i in range(5):
    gen()