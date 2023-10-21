import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
def Test_Post(driver, wait):
    driver.get('https://yarro.onrender.com')
    
    xlogin_username_field = "/html/body/main/div/div[2]/form/input[1]"
    xlogin_password_field = "/html/body/main/div/div[2]/form/div[2]/input[1]"
    xlogin_btn = "/html/body/main/div/div[2]/form/input[2]"
    
    xpost_box = "/html/body/main/div[4]/div/div[2]/input"
    xpost_area = "/html/body/main/div[1]/div/div/div/div[2]/p/textarea"
    xpost_btn = "/html/body/main/div[1]/div/div/div/div[3]/button[1]"
    xcancel_btn = "/html/body/main/div[1]/div/div/div/div[3]/button[2]"
    
    xoptions = "/html/body/main/div[5]/div[1]/div[1]/div[2]/div[1]/div/div/span"
    xdelete = "/html/body/main/div[5]/div[1]/div[1]/div[2]/div[1]/div/div/div/p"

    file = open(".\Post\post.json")
    post = json.load(file)['Post']
    test_cases = post['Test_Cases']    
    print()
    print(post['Test_Scenario'])
    
    action = ActionChains(driver)
    login_btn = wait.until(EC.presence_of_element_located((By.XPATH, xlogin_btn)))
    username = wait.until(EC.presence_of_element_located((By.XPATH, xlogin_username_field)))
    password = wait.until(EC.presence_of_element_located((By.XPATH, xlogin_password_field)))
    username.send_keys("Tory")
    password.send_keys("Tory@1234")
    action.click(login_btn).perform()
    time.sleep(5)

    for i in test_cases:
        print("Test ID - " + i["Test_Id"])
        post_box = wait.until(EC.presence_of_element_located((By.XPATH, xpost_box)))
        action.click(post_box).perform()
        post_area = wait.until(EC.presence_of_element_located((By.XPATH, xpost_area)))
        post_area.send_keys(i["Test_Data"]["Post_Message"])
        post_btn = wait.until(EC.presence_of_element_located((By.XPATH, xpost_btn)))
        action.click(post_btn).perform()
        time.sleep(6)
        try:
            options = wait.until(EC.presence_of_all_elements_located((By.XPATH, xoptions)))
            action.move_to_element(options[0]).perform()
            delete = wait.until(EC.presence_of_element_located((By.XPATH, xdelete)))
            action.click(delete).perform()
            time.sleep(4)
            if i["Test_Type"] == "positive":
                print("Test Pass")
        except NoSuchElementException as err:
            if i["Test_Type"] == "negative":
                print("Test Pass")
            else:
                print("Test Fails")
        
        




if __name__ == "__main__":
    pass