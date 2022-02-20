from selenium import webdriver
from supplier.login import loginPage
from supplier.offer import Offer
import time
driver = webdriver.Chrome('../chromedriver.exe')
driver.get('http://localhost:3000')
time.sleep(1)

login = loginPage()
login.loginUser(driver)

offer = Offer()
offer.OfferAccept(driver)

offer = Offer()
offer.OfferReject(driver)


print('Test Successful');

driver.close()