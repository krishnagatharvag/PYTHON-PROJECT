
import selenium
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://facebook.com")
time.sleep(3)
driver.find_element_by_id("email").send_keys("krishnakantg76@gmail.com")
time.sleep(3)
driver.find_element_by_id("pass").send_keys("Krishnaatharva2306@")
time.sleep(3)
driver.find_element_by_name("login").click()
# driver.get("https://www.hongkiat.com/blog/")
# time.sleep(3)
# use1=driver.find_element_by_xpath("//*[@id='design-dev-menu']/a")
# time.sleep(3)
# user2=driver.find_element_by_xpath("//*[@id='post-dropdown-29928]/a")
#
# action=ActionChains(driver)
# action.move_to_element(use1).move_to_element(user2).click().perform()

"""
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")
button=driver.find_element_by_xpath("//button[text()= 'Copy Text']")
action=ActionChains(driver)
action.double_click(button).perform()
"""
"""
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

"""
"""
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
"""


# import selenium
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver import ActionChains
# from webdriver_manager.chrome import ChromeDriverManager
# #driver=webdriver.Chrome(ChromeDriverManager().install())
# driver=webdriver.Chrome("C:\\Users\\KK\\.wdm\\drivers\\chromedriver\\win64\\116.0.5845.111\\chromedriver-win32\\chromedriver.exe")
# driver.get("https://testautomationpractice.blogspot.com/")
# ele=driver.find_element_by_xpath("//button[@onclick='myFunction()']")
# action=ActionChains(driver)
# action.double_click(ele).click().perform()


import selenium
import time
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
#driver=webdriver.Chrome(ChromeDriverManager().install())
driver=webdriver.Chrome("C:\\Users\\KK\\.wdm\\drivers\\chromedriver\\win64\\116.0.5845.111\\chromedriver-win32\\chromedriver.exe")
#driver.get("https://testautomationpractice.blogspot.com/")
driver.get("https://selectorshub.com/xpath-practice-page/")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("(//a[@aria-haspopup='true'])[1]").click()
time.sleep(5)
driver.find_element_by_xpath("(//a[@aria-haspopup='true'])[1][a][1]").click()
time.sleep(5)


