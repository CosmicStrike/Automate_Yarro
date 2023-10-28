import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time


def Test_Register(driver, waits, waitc, df):
    xsignup_btn = "/html/body/main/div/div[1]/form/input[5]"
    xemail_field = "/html/body/main/div/div[1]/form/input[1]"
    xsignup_username_field = "/html/body/main/div/div[1]/form/input[2]"
    xsignup_password_field = "/html/body/main/div/div[1]/form/input[3]"
    xreenterpassword_field = "/html/body/main/div/div[1]/form/input[4]"

    xconfirm = "/html/body/div/div/a"
    xsnnack_bar = "/html/body/div"

    file = open(".\SignUp\signup.json")
    test = json.load(file)['Test']
    test_cases = test['Test_Cases']
    print()
    print(test['Test_Scenario'])

    action = ActionChains(driver)

    for i in test_cases:
        driver.delete_all_cookies()
        driver.get('http://localhost:3000/register')

        signup_btn = waits.until(
            EC.presence_of_element_located((By.XPATH, xsignup_btn)))
        password = waits.until(EC.presence_of_element_located(
            (By.XPATH, xsignup_password_field)))
        repassword = waits.until(EC.presence_of_element_located(
            (By.XPATH, xreenterpassword_field)))
        email = waits.until(
            EC.presence_of_element_located((By.XPATH, xemail_field)))
        username = waits.until(EC.presence_of_element_located(
            (By.XPATH, xsignup_username_field)))
        print("Test ID - " + i["Test_Id"])
        username.clear()
        password.clear()
        repassword.clear()
        email.clear()

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
        repassword.send_keys(i["Test_Data"]["repassword"])
        email.send_keys(i["Test_Data"]["email"])
        time.sleep(1)

        action.click(signup_btn).perform()

        try:
            waitc.until(EC.presence_of_element_located((By.XPATH, xconfirm)))
            driver.delete_all_cookies()
            time.sleep(3)
            driver.back()
            df["Observed Outcome"].append("Successful Registration")
            if i["Test_Type"] == "positive":
                df["Status"].append("Pass")
                print("Test Pass")
            else:
                df["Status"].append("Fail")
                print("Test Fail")
        except (NoSuchElementException, TimeoutException) as err:
            time.sleep(3)
            df["Observed Outcome"].append("Registration Failed")
            if i["Test_Type"] == "negative":
                df["Status"].append("Pass")
                print("Test Pass")
            else:
                df["Status"].append("Fail")
                print("Test Fail")
        driver.delete_all_cookies()

    print("SignUp : ", df)
    return df


if __name__ == "__main__":
    pass
