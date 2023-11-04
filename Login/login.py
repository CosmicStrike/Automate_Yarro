import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time


def Test_Login(driver, waits, waitc, df):
    xlogin_username_field = "/html/body/main/div/div[2]/form/input[1]"
    xlogin_password_field = "/html/body/main/div/div[2]/form/div[2]/input[1]"
    xlogin_btn = "/html/body/main/div/div[2]/form/input[2]"

    xprofile_btn = "/html/body/header/div[2]/div/div[1]"
    xlogout_btn = "/html/body/header/div[2]/div/div[2]/p[2]"
    xsnnack_bar = "/html/body/div"

    file = open(".\Login\login.json")
    test = json.load(file)['Test']
    test_cases = test['Test_Cases']
    print()
    print(test['Test_Scenario'])
    action = ActionChains(driver)

    for i in test_cases:
        driver.delete_all_cookies()
        driver.get('http://localhost:3000/')

        login_btn = waits.until(
            EC.presence_of_element_located((By.XPATH, xlogin_btn)))
        username = waits.until(EC.presence_of_element_located(
            (By.XPATH, xlogin_username_field)))
        password = waits.until(EC.presence_of_element_located(
            (By.XPATH, xlogin_password_field)))

        username.clear()
        password.clear()

        print("Test ID - " + i["Test_Id"])

        df["Test Module"].append(test["Test_Module"])
        df["Test Case Id"].append(i["Test_Id"])
        df["Test Scenario"].append(test["Test_Scenario"])
        df["Test Description"].append(i["Description"])
        df["Test Precondition"].append(i["Pre_Condition"])
        df["Test Data"].append(str(i["Test_Data"]))
        df["Test Type"].append(i["Test_Type"])
        df["Expected Outcome"].append(i["Expected_Outcome"])

        username.send_keys(i["Test_Data"]["username"])
        password.send_keys(i["Test_Data"]["password"])
        time.sleep(1)
        action.click(login_btn).perform()
        time.sleep(2)

        try:
            profile_btn = waitc.until(
                EC.presence_of_element_located((By.XPATH, xprofile_btn)))
            action.move_to_element(profile_btn).perform()
            logout_btn = waits.until(
                EC.presence_of_element_located((By.XPATH, xlogout_btn)))
            action.click(logout_btn).perform()

            df["Observed Outcome"].append("Successful Login")
            if i["Test_Type"] == "positive":
                df["Status"].append("Pass")
                print("Test Pass")
            else:
                df["Status"].append("Fail")
                print("Test Fail")
        except (NoSuchElementException, TimeoutException) as err:
            df["Observed Outcome"].append("Login Failed")
            if i["Test_Type"] == "negative":
                df["Status"].append("Pass")
                print("Test Pass")
            else:
                df["Status"].append("Fail")
                print("Test Fail")
        driver.delete_all_cookies()

    print("Login : ", df)
    return df


if __name__ == "__main__":
    pass
