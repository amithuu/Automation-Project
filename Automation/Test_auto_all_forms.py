import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# from Automation.merge_file import Mrge

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

class Templates1():

    def templates1(self):
        driver.get("https://test-talentplace.vercel.app/login")

        # Login
        driver.find_element(By.NAME, "email").send_keys("muhsinny333@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("112233445566@As")
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        driver.maximize_window()
        # ref.merge()
        time.sleep(3)

ref = Templates1()
ref.templates1()