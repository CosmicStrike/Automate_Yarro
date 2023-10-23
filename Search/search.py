import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time


def Test_Search(driver, waits, waitc, df):

    xsearch_box = "/html/body/main/form/div/input[1]"
    xsearch_user = "/html/body/main/div"

    file = open(".\Search\search.json")
    test = json.load(file)['Test']
    test_cases = test['Test_Cases']
    print()
    print(test['Test_Scenario'])

    driver.get('http://localhost:3000/search')
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

        search_box = waits.until(
            EC.presence_of_element_located((By.XPATH, xsearch_box)))
        search_box.clear()
        search_box.send_keys(i["Test_Data"]["username"])
        time.sleep(1)

        action.send_keys_to_element(search_box, Keys.ENTER).perform()
        time.sleep(4)

        search_users = waits.until(
            EC.presence_of_element_located((By.XPATH, xsearch_user)))
        tot_users = search_users.find_elements(By.XPATH, "*")

        time.sleep(2)
        df["Observed Outcome"].append(str(len(tot_users)) + " User found")
        df["Status"].append("Pass")
        print("Test Pass")

    print("Search : ", df)
    return df


if __name__ == "__main__":
    pass
