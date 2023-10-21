import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
def Test_Chat(driver, wait):
    driver.get('https://yarro.onrender.com')
    
    xlogin_username_field = "/html/body/main/div/div[2]/form/input[1]"
    xlogin_password_field = "/html/body/main/div/div[2]/form/div[2]/input[1]"
    xlogin_btn = "/html/body/main/div/div[2]/form/input[2]"
    
    xchat_user = "/html/body/main/div/div/div[1]/ul/li/a[5]"
    xchat_box = "/html/body/main/div/div/div[2]/div/div[3]/input"
    imsg_list = "msg_list"
    xsend_btn = "/html/body/main/div/div/div[2]/div/div[3]/button"
    ximg_list = "/html/body/main/div/div/div[2]/div/div[2]/ul/li"
    file = open(".\Chat\chat.json")
    chat = json.load(file)['Chat']
    test_cases = chat['Test_Cases']    
    print()
    print(chat['Test_Scenario'])
    
    action = ActionChains(driver)
    login_btn = wait.until(EC.presence_of_element_located((By.XPATH, xlogin_btn)))
    username = wait.until(EC.presence_of_element_located((By.XPATH, xlogin_username_field)))
    password = wait.until(EC.presence_of_element_located((By.XPATH, xlogin_password_field)))
    username.send_keys("Tory")
    password.send_keys("Tory@1234")
    action.click(login_btn).perform()
    time.sleep(5)

    driver.get('https://yarro.onrender.com/chat')


    for i in test_cases:
        print("Test ID - " + i["Test_Id"])
        chat_user = wait.until(EC.presence_of_element_located((By.XPATH, xchat_user)))
        action.click(chat_user).perform()
        chat_box = wait.until(EC.presence_of_element_located((By.XPATH, xchat_box)))
        send_btn = wait.until(EC.presence_of_element_located((By.XPATH, xsend_btn)))
        action.send_keys_to_element(chat_box, i["Test_Data"]["Message"]).perform()
        action.click(send_btn).perform()
        time.sleep(4)
        try:
            msg_list = wait.until(EC.presence_of_all_elements_located((By.XPATH, ximg_list)))
            print(len(msg_list))
            if i["Test_Type"] == "positive":
                print("Test Pass")           
        except NoSuchElementException as err:
            if i["Test_Type"] == "negative":
                print("Test Pass")
            else:
                print("Test Fails")
        
        




if __name__ == "__main__":
    pass