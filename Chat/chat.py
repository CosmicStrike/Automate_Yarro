import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time


def Test_Chat(driver, waits, waitc, df):
    xchat_user = "/html/body/main/div/div/div[1]/ul/li/a[1]"
    xchat_box = "/html/body/main/div/div/div[2]/div/div[3]/input"

    xsend_btn = "/html/body/main/div/div/div[2]/div/div[3]/button"
    xmsg_list = "/html/body/main/div/div/div[2]/div/div[2]/ul"

    file = open(".\Chat\chat.json")
    test = json.load(file)['Test']
    test_cases = test['Test_Cases']
    print()
    print(test['Test_Scenario'])

    driver.get('http://localhost:3000/chat')
    action = ActionChains(driver)

    for i in test_cases:
        print("Test ID - " + i["Test_Id"])

        df["Test Module"].append(test["Test_Module"])
        df["Test Case Id"].append(i["Test_Id"])
        df["Test Scenario"].append(test["Test_Scenario"])
        df["Test Description"].append(i["Description"])
        df["Test Precondition"].append(i["Pre_Condition"])
        df["Test Data"].append(str(i["Test_Data"]))
        df["Test Type"].append(i["Test_Type"])
        df["Expected Outcome"].append(i["Expected_Outcome"])

        chat_user = waits.until(
            EC.presence_of_element_located((By.XPATH, xchat_user)))
        action.click(chat_user).perform()

        msg_list = waits.until(
            EC.presence_of_element_located((By.XPATH, xmsg_list)))
        tot_msg_bef = msg_list.find_elements(By.XPATH, "*")
        before_msg = len(tot_msg_bef)

        chat_box = waits.until(
            EC.presence_of_element_located((By.XPATH, xchat_box)))
        chat_box.clear()
        send_btn = waits.until(
            EC.presence_of_element_located((By.XPATH, xsend_btn)))
        action.send_keys_to_element(
            chat_box, i["Test_Data"]["Message"]).perform()
        time.sleep(1)
        action.click(send_btn).perform()

        msg_list = waits.until(
            EC.presence_of_element_located((By.XPATH, xmsg_list)))
        tot_msg_aft = msg_list.find_elements(By.XPATH, "*")
        after_msg = len(tot_msg_aft)

        time.sleep(4)
        if before_msg == after_msg and i["Test_Type"] == "negative":
            print("Test Pass")
            df["Status"].append("Pass")
            df["Observed Outcome"].append("Failed to send the message")
        elif (after_msg - 1) == before_msg and i["Test_Type"] == "positive":
            df["Observed Outcome"].append("Successfully send the message")
            df["Status"].append("Pass")
            print("Test Pass")
        else:
            df["Observed Outcome"].append("Failed to send the message")
            df["Status"].append("Fail")
            print("Test Fail")

    print(df)
    return df


if __name__ == "__main__":
    pass
