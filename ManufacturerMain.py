from selenium import webdriver
from manufacturer.login import loginPage
from manufacturer.addLicense import Add_License
import time
driver = webdriver.Chrome('../chromedriver.exe')
driver.get('http://localhost:3000')
time.sleep(1)

login = loginPage()
login.loginUser(driver)

license = Add_License()
license.Add(driver)



print('sleep')
