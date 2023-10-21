import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
def Test_Profile(driver, wait):
    driver.get('https://yarro.onrender.com')
    
    xlogin_username_field = "/html/body/main/div/div[2]/form/input[1]"
    xlogin_password_field = "/html/body/main/div/div[2]/form/div[2]/input[1]"
    xlogin_btn = "/html/body/main/div/div[2]/form/input[2]"
    
    xprofile_logo = "/html/body/header/div[2]/div/div[1]"
    xprofile_btn = "/html/body/header/div[2]/div/div[2]/p[1]"
    xlogout_btn = "/html/body/header/div[2]/div/div[2]/p[2]"

    xedit_profile_btn = "/html/body/main/div[1]/div/div[2]/div/div[1]/div/button"

    xname = "/html/body/main/div/form/div[1]/input"
    xbio = "/html/body/main/div/form/div[5]/textarea"
    xmobile = "/html/body/main/div/form/div[3]/input"
    xsave_btn = "/html/body/main/div/form/div[6]/input"

    xsnnack_bar = "/html/body/div"

    file = open(".\Profile\profile.json")
    profile = json.load(file)['Profile']
    test_cases = profile['Test_Cases']    
    print()
    print(profile['Test_Scenario'])
    
    action = ActionChains(driver)
    login_btn = wait.until(EC.presence_of_element_located((By.XPATH, xlogin_btn)))
    username = wait.until(EC.presence_of_element_located((By.XPATH, xlogin_username_field)))
    password = wait.until(EC.presence_of_element_located((By.XPATH, xlogin_password_field)))
    username.send_keys("Tory")
    password.send_keys("Tory@1234")
    action.click(login_btn).perform()

    profile_logo = wait.until(EC.presence_of_element_located((By.XPATH, xprofile_logo)))
    action.move_to_element(profile_logo).perform()
    profile_btn = wait.until(EC.presence_of_element_located((By.XPATH, xprofile_btn)))
    action.click(profile_btn).perform()

    edit_profile_btn = wait.until(EC.presence_of_element_located((By.XPATH, xedit_profile_btn)))
    action.click(edit_profile_btn).perform()
    time.sleep(4)

    name = wait.until(EC.presence_of_element_located((By.XPATH, xname)))
    mobile = wait.until(EC.presence_of_element_located((By.XPATH, xmobile)))
    bio = wait.until(EC.presence_of_element_located((By.XPATH, xbio)))
    save_btn = wait.until(EC.presence_of_element_located((By.XPATH, xsave_btn)))
    for i in test_cases:
        print("Test ID - " + i["Test_Id"])
        action.send_keys_to_element(name, "").perform()
        action.send_keys_to_element(mobile, "").perform()
        action.send_keys_to_element(bio, "").perform()
        action.send_keys_to_element(name, i["Test_Data"]["name"]).perform()
        action.send_keys_to_element(mobile, i["Test_Data"]["mobile"]).perform()
        action.send_keys_to_element(bio, i["Test_Data"]["bio"]).perform()
        action.click(save_btn).perform()
        try:
            snackbar = wait.until(EC.presence_of_element_located((By.XPATH, xsnnack_bar)))
            childs = snackbar.find_elements(By.XPATH, "*")
            for c in childs:
                print(c.text)
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