import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time


def Test_Post(driver,  waits, waitc, df):

    xpost_box = "/html/body/main/div[4]/div/div[2]/input"
    xpost_area = "/html/body/main/div[1]/div/div/div/div[2]/p/textarea"
    xpost_btn = "/html/body/main/div[1]/div/div/div/div[3]/button[1]"

    xoptions = "/html/body/main/div[5]/div[1]/div[1]/div[2]/div[1]/div/div/span"
    xdelete = "/html/body/main/div[5]/div[1]/div[1]/div[2]/div[1]/div/div/div/p"

    xpost_bundle = "/html/body/main/div[5]"
    xpost_like_btn = "/html/body/main/div[5]/div[1]/div[3]/div[1]/span"
    xpost_like_cnt = "/html/body/main/div[5]/div[1]/div[3]/div[1]/p"
    xpost_close_btn = "/html/body/main/div[1]/div/div/div/div[3]/button[2]"

    xpost_dislike_cnt = "/html/body/main/div[5]/div[1]/div[3]/div[2]/p"
    xpost_dislike_btn = "/html/body/main/div[5]/div[1]/div[3]/div[2]/span"
    file = open(".\Post\post.json")
    test = json.load(file)['Test']
    test_cases = test['Test_Cases']
    print()
    print(test['Test_Scenario'])

    driver.get("http://localhost:3000")
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

        post_bundle = waits.until(
            EC.presence_of_element_located((By.XPATH, xpost_bundle)))
        tot_post = post_bundle.find_elements(By.XPATH, "*")
        init_post_len = len(tot_post)

        post_box = waits.until(
            EC.presence_of_element_located((By.XPATH, xpost_box)))
        action.click(post_box).perform()
        time.sleep(1)
        post_area = waits.until(
            EC.presence_of_element_located((By.XPATH, xpost_area)))
        post_area.send_keys(i["Test_Data"]["Post_Message"])
        time.sleep(1)
        post_btn = waits.until(
            EC.presence_of_element_located((By.XPATH, xpost_btn)))
        action.click(post_btn).perform()
        time.sleep(1)

        post_bundle = waits.until(
            EC.presence_of_element_located((By.XPATH, xpost_bundle)))
        tot_post = post_bundle.find_elements(By.XPATH, "*")
        after_post_len = len(tot_post)
        print(init_post_len)
        print(after_post_len)
        try:
            if init_post_len == (after_post_len - 1):
                # Like the post
                post_like_btn = waits.until(
                    EC.presence_of_element_located((By.XPATH, xpost_like_btn)))
                time.sleep(1)

                post_like_cnt = waits.until(
                    EC.presence_of_element_located((By.XPATH, xpost_like_cnt)))
                before_like = int(post_like_cnt.text)
                time.sleep(1)

                action.click(post_like_btn).perform()
                time.sleep(1)

                post_like_cnt = waits.until(
                    EC.presence_of_element_located((By.XPATH, xpost_like_cnt)))
                after_like = int(post_like_cnt.text)
                time.sleep(1)
                print("Tested Like")
                if before_like != after_like - 1:
                    df["Status"].append("Fail")
                    raise Exception("Like")
                time.sleep(1)
                # Dislike the post
                post_dislike_btn = waits.until(
                    EC.presence_of_element_located((By.XPATH, xpost_dislike_btn)))
                post_dislike_cnt = waits.until(
                    EC.presence_of_element_located((By.XPATH, xpost_dislike_cnt)))
                time.sleep(1)

                before_dislike = int(post_dislike_cnt.text)
                time.sleep(1)

                action.click(post_dislike_btn).perform()
                post_dislike_cnt = waits.until(
                    EC.presence_of_element_located((By.XPATH, xpost_dislike_cnt)))
                time.sleep(1)

                after_dislike = int(post_dislike_cnt.text)
                print(before_dislike)
                print(after_dislike)
                print("Tested Dislike")

                if before_dislike != after_dislike - 1:
                    df["Status"].append("Fail")
                    raise Exception("Dislike")
                time.sleep(1)

                options = waitc.until(
                    EC.presence_of_all_elements_located((By.XPATH, xoptions)))
                action.move_to_element(options[0]).perform()
                time.sleep(1)

                delete = waits.until(
                    EC.presence_of_element_located((By.XPATH, xdelete)))
                time.sleep(1)

                action.click(delete).perform()
                df["Observed Outcome"].append(
                    "Successfully created and deleted post")

                if i["Test_Type"] == "positive":
                    df["Status"].append("Pass")
                    print("Test Pass")
                elif i["Test_Type"] == "negative":
                    df["Status"].append("Fail")
                    print("Test Fail")
            else:
                print("Failed to clrate post")
                post_close_btn = waits.until(
                    EC.presence_of_element_located((By.XPATH, xpost_close_btn)))
                time.sleep(2)
                action.click(post_close_btn).perform()
                time.sleep(2)

                df["Observed Outcome"].append(
                    "Failed to create the post")
                if i["Test_Type"] == "positive":
                    df["Status"].append("Fail")
                    print("Test Fail")
                elif i["Test_Type"] == "negative":
                    df["Status"].append("Pass")
                    print("Test Pass")

        except (NoSuchElementException, TimeoutException) as err:
            df["Observed Outcome"].append(
                "Failed to create the post,web element not found while testing")
            df["Status"].append("Fail")
            print("Test Fail")

        except Exception as err:
            if err.args.__contains__("Like"):
                df["Observed Outcome"].append(
                    "Failed to like the post")
            elif err.args.__contains__("Dislike"):
                df["Observed Outcome"].append(
                    "Failed to Dislike the post")

        time.sleep(4)
    print("Post : ", df)
    return df


if __name__ == "__main__":
    pass
