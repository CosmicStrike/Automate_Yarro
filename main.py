# selenium 4
from Login.login import Test_Login
from SignUp.signup import Test_Register
from Post.post import Test_Post
from Search.search import Test_Search
from Chat.chat import Test_Chat
from Profile.profile import Test_Profile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.core.driver_cache import DriverCacheManager
import os

if __name__ == "__main__":    
    os.environ['WDM_LOCAL'] = '1'
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(cache_manager=DriverCacheManager(valid_range=10)).install()))
    wait = WebDriverWait(driver,300)

    # Test_Login(driver, wait)
    # Test_Register(driver, wait)
    # Test_Post(driver, wait)
    # Test_Search(driver, wait)
    # Test_Chat(driver, wait)
    Test_Profile(driver, wait)


