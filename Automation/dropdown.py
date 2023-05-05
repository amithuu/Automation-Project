# this we can use it for single drop down
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By


class Dropdown():

    def drop_down(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.talentplace.ai/sign-up")

        drop=driver.find_element(By.NAME,"gender")
        dd=Select(drop)

        dd.select_by_index(2)
        time.sleep(2)
        dd.select_by_value("male")
        time.sleep(2)
        dd.select_by_visible_text("Prefer Not To Mention")
        time.sleep(2)

ref = Dropdown()
ref.drop_down()

# values=['male','female']
#
# for i in values:
#     ret=values[0]
#     if ret=='male':
#         break
# print(ret)
# # /ind=values.index('female')
# # print(ind)

