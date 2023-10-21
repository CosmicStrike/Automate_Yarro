import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
def Test_Login(driver, wait):
    driver.get('https://yarro.onrender.com')

    xlogin_username_field = "/html/body/main/div/div[2]/form/input[1]"
    xlogin_password_field = "/html/body/main/div/div[2]/form/div[2]/input[1]"
    xlogin_btn = "/html/body/main/div/div[2]/form/input[2]"
    
    xprofile_btn = "/html/body/header/div[2]/div/div[1]"
    xlogout_btn = "/html/body/header/div[2]/div/div[2]/p[2]"
    
    xforgotpassword_btn = "/html/body/main/div/div[1]/form/input[2]"
    xforgotpassword_email_field = "/html/body/main/div/div[1]/form/input[1]"

    file = open(".\Login\login.json")
    login = json.load(file)['Login']
    test_cases = login['Test_Cases']    
    print()
    print(login['Test_Scenario'])
    action = ActionChains(driver)
    for i in test_cases:
        print("Test ID - " + i["Test_Id"])
        login_btn = wait.until(EC.presence_of_element_located((By.XPATH, xlogin_btn)))
        username = wait.until(EC.presence_of_element_located((By.XPATH, xlogin_username_field)))
        password = wait.until(EC.presence_of_element_located((By.XPATH, xlogin_password_field)))
        username.send_keys(i["Test_Data"]["username"])
        password.send_keys(i["Test_Data"]["password"])
        action.click(login_btn).perform()
        time.sleep(5)
        try:
            profile_btn = driver.find_element(By.XPATH, xprofile_btn)
            action.move_to_element(profile_btn).perform()
            logout_btn =  wait.until(EC.presence_of_element_located((By.XPATH, xlogout_btn)))
            action.click(logout_btn).perform()
            if i["Test_Type"] == "positive":
                print("Test Pass")
            else:
                print("Test Fail")
        except NoSuchElementException as err:
            if i["Test_Type"] == "negative":
                print("Test Pass")
            else:
                print("Test Fails")
            
        




if __name__ == "__main__":
    pass