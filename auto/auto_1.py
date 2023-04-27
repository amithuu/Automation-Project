from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

import time

class Auto():

    def auto_mate(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https:google.com")
        print(driver.title)

ref=Auto()
ref.auto_mate()