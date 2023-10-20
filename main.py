# selenium 4
from Login.login import Test_Login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


if __name__ == "__main__":    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    wait = WebDriverWait(driver,600)

    driver.get('https://yarro.onrender.com')
    Test_Login(driver, wait)

