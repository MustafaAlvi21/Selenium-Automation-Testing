import time


class Offer():

    def OfferAccept(self, driver):
        offerLink = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/div/div/ul/li[6]/a')
        offerLink.click()
        time.sleep(3)


        selectBTN = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[3]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]/div/div/a')
        optionBTN = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[3]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]/div/div/div/a[2]')

        selectBTN.click()
        time.sleep(3)
        optionBTN.click()

        time.sleep(5)


    def OfferReject(self, driver):
        offerLink = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/div/div/ul/li[6]/a')
        offerLink.click()
        time.sleep(3)


        selectBTN = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[3]/div/div[2]/div/div/div[2]/table/tbody/tr[2]/td[1]/div/div/a')
        optionBTN = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[3]/div/div[2]/div/div/div[2]/table/tbody/tr[2]/td[1]/div/div/div/a[3]')

        selectBTN.click()
        time.sleep(3)
        optionBTN.click()

        time.sleep(5)


