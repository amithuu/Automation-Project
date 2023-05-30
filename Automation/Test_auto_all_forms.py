import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# from Automation.merge_file import Mrge

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

class Templa:

    def templa(self):
        driver.get("https://test-talentplace.vercel.app/login")

        # Login
        driver.find_element(By.NAME, "email").send_keys("muhsinny333@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("112233445566@As")
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        driver.maximize_window()
        # ref.merge()
        time.sleep(3)


ref = Templa()
ref.templa()
