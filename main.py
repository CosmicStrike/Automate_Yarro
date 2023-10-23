# selenium 4
from Login.login import Test_Login
from SignUp.signup import Test_Register
from Post.post import Test_Post
from Search.search import Test_Search
from Chat.chat import Test_Chat
from Profile.profile import Test_Profile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.core.driver_cache import DriverCacheManager
import os
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support import expected_conditions as EC


def Report(df, folder, filename):
    path = '/'.join([folder, folder+"_Test_Report.xlsx"])
    df.to_excel(path)
    print(path)
    pass


if __name__ == "__main__":
    os.environ['WDM_LOCAL'] = '1'
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
        cache_manager=DriverCacheManager(valid_range=10)).install()))
    wait_toshow = WebDriverWait(driver, 60)
    wait_tocheck = WebDriverWait(driver, 10)
    df = {"Test Module": [], "Test Case Id": [], "Test Scenario": [], "Test Description": [], "Test Precondition": [
    ], "Test Data": [], "Test Type": [], "Expected Outcome": [], "Observed Outcome": [], "Status": []}

    Test_Login(driver, wait_toshow, wait_tocheck, df)
    time.sleep(2)
    driver.delete_all_cookies()

    Test_Register(driver, wait_toshow, wait_tocheck, df)
    time.sleep(2)
    driver.get('http://localhost:3000')
    driver.delete_all_cookies()

    xlogin_username_field = "/html/body/main/div/div[2]/form/input[1]"
    xlogin_password_field = "/html/body/main/div/div[2]/form/div[2]/input[1]"
    xlogin_btn = "/html/body/main/div/div[2]/form/input[2]"
    xprofile_btn = "/html/body/header/div[2]/div/div[1]"
    try:
        action = ActionChains(driver)
        login_btn = wait_toshow.until(
            EC.presence_of_element_located((By.XPATH, xlogin_btn)))
        username = wait_toshow.until(
            EC.presence_of_element_located((By.XPATH, xlogin_username_field)))
        password = wait_toshow.until(
            EC.presence_of_element_located((By.XPATH, xlogin_password_field)))
        username.send_keys("Tester")
        password.send_keys("Test@1234")
        action.click(login_btn).perform()
        profile_btn = wait_tocheck.until(
            EC.presence_of_element_located((By.XPATH, xprofile_btn)))
        time.sleep(2)
        Test_Post(driver, wait_toshow, wait_tocheck, df)
        time.sleep(2)
        Test_Search(driver, wait_toshow, wait_tocheck, df)
        time.sleep(2)
        Test_Chat(driver, wait_toshow, wait_tocheck, df)
        time.sleep(2)
        Test_Profile(driver, wait_toshow, wait_tocheck, df)
        time.sleep(2)
        for i in df:
            print(len(df[i]))
        report = pd.DataFrame(df)
        report.to_excel('Report.xlsx')

    except (NoSuchElementException, TimeoutException) as err:
        print("Testing Failed")
