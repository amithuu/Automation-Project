from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
import time
class Date():

    def date_auto(self):

        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.talentplace.ai/sign-up")
        driver.find_element(By.NAME,"dob").send_keys("08/10/2021")
        time.sleep(5)
ref=Date()
ref.date_auto()



