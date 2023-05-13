import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())

class Mrge:

    def merge(self):

        # Click on Templates
        # ref.templates1()
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//p[text()='Templates']"))).click()
        # time.sleep(3)


ref = Mrge()
ref.merge()
