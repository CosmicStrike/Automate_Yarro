import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
def Test_Search(driver, wait):
    driver.get('https://yarro.onrender.com')
    
    xlogin_username_field = "/html/body/main/div/div[2]/form/input[1]"
    xlogin_password_field = "/html/body/main/div/div[2]/form/div[2]/input[1]"
    xlogin_btn = "/html/body/main/div/div[2]/form/input[2]"
    
    xsearch_box = "/html/body/main/form/div/input[1]"
    xsearch_user = "/html/body/main/div/a"

    file = open(".\Search\search.json")
    search = json.load(file)['Search']
    test_cases = search['Test_Cases']    
    print()
    print(search['Test_Scenario'])
    
    action = ActionChains(driver)
    login_btn = wait.until(EC.presence_of_element_located((By.XPATH, xlogin_btn)))
    username = wait.until(EC.presence_of_element_located((By.XPATH, xlogin_username_field)))
    password = wait.until(EC.presence_of_element_located((By.XPATH, xlogin_password_field)))
    username.send_keys("Tory")
    password.send_keys("Tory@1234")
    action.click(login_btn).perform()
    time.sleep(5)

    driver.get('https://yarro.onrender.com/search')


    for i in test_cases:
        print("Test ID - " + i["Test_Id"])
        search_box = wait.until(EC.presence_of_element_located((By.XPATH, xsearch_box)))
        search_box.send_keys(i["Test_Data"]["username"])
        action.send_keys_to_element(search_box, Keys.ENTER).perform()
        time.sleep(6)
        try:
            search_users = driver.find_elements(By.XPATH, xsearch_user)
            print(len(search_users))
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