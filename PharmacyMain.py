from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pharmacy.register import registerPage
from pharmacy.login import loginPage
from pharmacy.createOffer import CreateOffer
import time

s = Service('C:/Users/Alvi/PycharmProjects/chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get('http://localhost:3000')
time.sleep(1)

register = registerPage()
register.registerUser(driver)

login = loginPage()
login.loginUser(driver)

offer = CreateOffer()
offer.Create(driver)


print('  /*******************************/');
print(' /*       Test Successful       */');
print('/*******************************/');

driver.close()