import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
def Test_Login(diver, wait):
    login_username_field = "/html/body/main/div/div[2]/form/input[1]"
    login_password_field = "/html/body/main/div/div[2]/form/div[2]/input[1]"
    login_btn = "/html/body/main/div/div[2]/form/input[2]"
    
    profile_btn = "/html/body/header/div[2]/div/div[2]/p[1]"
    logout_btn = "/html/body/header/div[2]/div/div[2]/p[2]"
    
    signup_btn = "/html/body/main/div/div[1]/form/input[5]"
    email_field = "/html/body/main/div/div[1]/form/input[1]"
    signup_username_field = "/html/body/main/div/div[1]/form/input[2]"
    signup_password_field = "/html/body/main/div/div[1]/form/input[3]"
    reenterpassword_field = "/html/body/main/div/div[1]/form/input[4]"

    forgotpassword_btn = "/html/body/main/div/div[1]/form/input[2]"
    forgotpassword_email_field = "/html/body/main/div/div[1]/form/input[1]"

    file = open(".\Login\login.json")
    login = json.load(file)['Login']
    test_cases = login['Test_Cases']    
    print()
    print(login['Test_Scenario'])
    # time.sleep(5)
    wait.until(EC.presence_of_element_located((By.XPATH, login_btn)))
    for i in test_cases:
        print("Test ID - " + i["Test_Id"])
        username = wait.until(EC.presence_of_element_located((By.XPATH, login_username_field)))
        password = wait.until(EC.presence_of_element_located((By.XPATH, login_password_field)))
        username.send_keys(i["Test_Data"]["username"])
        password.send_keys(i["Test_Data"]["password"])
        time.sleep(2)


if __name__ == "__main__":
    pass