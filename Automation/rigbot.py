import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Bug:

    def bug(self):
        driver= webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://app-test.rigbot.com")
        driver.maximize_window()
        time.sleep(10)

        #login
        name = driver.find_element(By.XPATH, "//input[@name='username']")
        name.send_keys("amithdm")
        time.sleep(2)
        name.send_keys(Keys.CONTROL +"a")
        name.send_keys("amith")
        time.sleep(3)
        # driver.find_element(By.XPATH, "//input[@name='username']").send_keys("amithdm")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("ami123")
        driver.find_element(By.XPATH, "//button[text()='Log In']").click()
        time.sleep(30)

        #Load Add Option
        driver.find_element(By.XPATH, "//a[@aria-label='Load add']").click()
        time.sleep(5)

        for i in range(1,8):
            flow = driver.find_element(By.XPATH, f"//*[@class='arrow-steps clearfix']/div[{i}]").click()
            time.sleep(2)
        for j in reversed(range(1, 7,)):
            flow = driver.find_element(By.XPATH, f"//*[@class='arrow-steps clearfix']/div[{j}]").click()
            time.sleep(2)


ref = Bug()
ref.bug()


