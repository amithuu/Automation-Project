import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
class Cerner():

    def cerner(self):
        driver.get("https://www.cerner.com")
        driver.maximize_window()
        print(driver.title)
        page_down = driver.find_element(By.TAG_NAME, value="body")

        page_down.send_keys(Keys.PAGE_DOWN)
        page_down.send_keys(Keys.PAGE_DOWN)
        page_down.send_keys(Keys.PAGE_DOWN)
        page_down.send_keys(Keys.PAGE_DOWN)
        page_down.send_keys(Keys.PAGE_DOWN)
        page_down.send_keys(Keys.PAGE_DOWN)
        page_down.send_keys(Keys.PAGE_DOWN)
        page_down.send_keys(Keys.PAGE_DOWN)
        time.sleep(4)
        region = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='regionSelector']")))
        region.click()
        list1 = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//a[text()='India']")))
        list1.click()
        driver.get_screenshot_as_file("C:/Users/Amith/Pictures/Screenshots.image.png")

        driver.close()


ref = Cerner()
ref.cerner()



