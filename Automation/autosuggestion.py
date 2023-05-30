# this we can use it for single drop down
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By


class Auto_sugg():

    def auto_sugg(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.talentplace.ai/sign-up")

        at=driver.find_element(By.NAME,"location")
        at.click()
        time.sleep(2)
        # at.clear()
        # time.sleep(3)
        at.send_keys("Bangalore, Karnataka, India")
        time.sleep(3)
        at.send_keys(Keys.ENTER)
        time.sleep(3)
        at.screenshot("desktop.png")





att=Auto_sugg()
att.auto_sugg()

