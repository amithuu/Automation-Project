from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


class Drop_down_React():

    def drop_react(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://test-talentplace.vercel.app/login")

        driver.find_element(By.NAME, "email").send_keys("amithkulkarni99@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("New@1234")
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(5)
        driver.maximize_window()

        # click on edit profile
        driver.find_element(By.XPATH, "//p[normalize-space()='Edit Profile']").click()
        time.sleep(2)

        # GO to personal details
        driver.find_element(By.XPATH, "//p[normalize-space()='Personal Details']").click()
        time.sleep(2)

        # option = driver.find_element(By.XPATH, "//div[@class=' css-1dimb5e-singleValue'][1]")
        # driver.execute_script("arguments[0].scrollIntoView();", option)
        # option.click()

        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                                    "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2)"))).click()
        time.sleep(3)
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,"//div[@class='chakra-form-control css-rps073']//div[@class=' css-19bb58m'] and text()='Male']"))).click()

# driver.find_element(By.XPATH, "//div[@class='chakra-form-control css-rps073']//div[@class=' css-19bb58m']").send_keys(Keys.ENTER)
ref = Drop_down_React()
ref.drop_react()
