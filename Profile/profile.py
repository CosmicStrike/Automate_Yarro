import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time


def Test_Profile(driver, waits, waitc, df):

    xprofile_logo = "/html/body/header/div[2]/div/div[1]"
    xprofile_btn = "/html/body/header/div[2]/div/div[2]/p[1]"

    xedit_profile_btn = "/html/body/main/div[1]/div/div[2]/div/div[1]/div/button"

    xname = "/html/body/main/div/form/div[1]/input"
    xbio = "/html/body/main/div/form/div[5]/textarea"
    xmobile = "/html/body/main/div/form/div[3]/input"
    xsave_btn = "/html/body/main/div/form/div[6]/input"

    xsnnack_bar = "/html/body/div"

    file = open(".\Profile\profile.json")
    test = json.load(file)['Test']
    test_cases = test['Test_Cases']
    print()
    print(test['Test_Scenario'])

    driver.get("http://localhost:3000")
    action = ActionChains(driver)

    profile_logo = waits.until(
        EC.presence_of_element_located((By.XPATH, xprofile_logo)))
    action.move_to_element(profile_logo).perform()
    profile_btn = waits.until(
        EC.presence_of_element_located((By.XPATH, xprofile_btn)))
    action.click(profile_btn).perform()
    time.sleep(2)
    edit_profile_btn = waits.until(
        EC.presence_of_element_located((By.XPATH, xedit_profile_btn)))
    action.click(edit_profile_btn).perform()
    time.sleep(2)

    name = waits.until(EC.presence_of_element_located((By.XPATH, xname)))
    mobile = waits.until(EC.presence_of_element_located((By.XPATH, xmobile)))
    bio = waits.until(EC.presence_of_element_located((By.XPATH, xbio)))
    save_btn = waits.until(
        EC.presence_of_element_located((By.XPATH, xsave_btn)))

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

        name.clear()
        mobile.clear()
        bio.clear()

        action.send_keys_to_element(name, i["Test_Data"]["name"]).perform()
        action.send_keys_to_element(mobile, i["Test_Data"]["mobile"]).perform()
        action.send_keys_to_element(bio, i["Test_Data"]["bio"]).perform()
        time.sleep(1)
        action.click(save_btn).perform()

        snackbar = waits.until(
            EC.presence_of_element_located((By.XPATH, xsnnack_bar)))
        childs = snackbar.find_elements(By.XPATH, "*")
        res = childs[0].text
        time.sleep(1)
        if res == "success":
            df["Observed Outcome"].append("Successful to change the profile")
        else:
            df["Observed Outcome"].append("Failed to change the profile")
        time.sleep(1)
        if res == "success" and i["Test_Type"] == "positive":
            df["Status"].append("Pass")
            print("Test Pass")
        else:
            df["Status"].append("Fail")
            print("Test Fail")

    print("Profile : ", df)
    return df


if __name__ == "__main__":
    pass
