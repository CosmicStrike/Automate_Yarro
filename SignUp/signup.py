import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
def Test_Register(driver, wait):
    driver.get('https://yarro.onrender.com/register')
    
    xsignup_btn = "/html/body/main/div/div[1]/form/input[5]"
    xemail_field = "/html/body/main/div/div[1]/form/input[1]"
    xsignup_username_field = "/html/body/main/div/div[1]/form/input[2]"
    xsignup_password_field = "/html/body/main/div/div[1]/form/input[3]"
    xreenterpassword_field = "/html/body/main/div/div[1]/form/input[4]"

    xforgotpassword_btn = "/html/body/main/div/div[1]/form/input[2]"
    xforgotpassword_email_field = "/html/body/main/div/div[1]/form/input[1]"

    file = open(".\SignUp\signup.json")
    signup = json.load(file)['SignUp']
    test_cases = signup['Test_Cases']    
    print()
    print(signup['Test_Scenario'])
    action = ActionChains(driver)
    for i in test_cases:
        print("Test ID - " + i["Test_Id"])
        signup_btn = wait.until(EC.presence_of_element_located((By.XPATH, xsignup_btn)))
        username = wait.until(EC.presence_of_element_located((By.XPATH, xsignup_username_field)))
        password = wait.until(EC.presence_of_element_located((By.XPATH, xsignup_password_field)))
        repassword = wait.until(EC.presence_of_element_located((By.XPATH, xreenterpassword_field)))
        email = wait.until(EC.presence_of_element_located((By.XPATH, xemail_field)))
        
        username.send_keys(i["Test_Data"]["username"])
        password.send_keys(i["Test_Data"]["password"])
        repassword.send_keys(i["Test_Data"]["repassword"])
        email.send_keys(i["Test_Data"]["email"])
        action.click(signup_btn).perform()
        time.sleep(5)
        try:
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