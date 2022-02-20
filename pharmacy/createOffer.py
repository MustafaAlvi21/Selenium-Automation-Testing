import time


class CreateOffer():

    def Create(self, driver):
        print("=> Login to Dashboard")

        marketField = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/div/div/ul/li[3]/a')
        marketField.click()
        time.sleep(3)

        print("==>> Dashboard to Marketplace")
        drugCard = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/section/div/div/div[2]/div/div[1]/div/div[5]/a')
        driver.execute_script("arguments[0].click();", drugCard)

        print("==>> Market to Drug Details")

        time.sleep(3)


        print("==>> Entering Offer Details")
        offerPrice = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/section[1]/div/div/div[2]/div[14]/input[1]')
        quantity = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/section[1]/div/div/div[2]/div[14]/input[2]')
        offerNow = driver.find_element_by_class_name('buyBtn')

        offerPrice.send_keys("1")
        time.sleep(1)
        quantity.send_keys("1")
        # offerNow.click()
        driver.execute_script("arguments[0].click();", offerNow)

        print("==>> Offer Added")


        time.sleep(10)

        gotoHome = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[1]/nav/div/div/div/a[1]")
        driver.execute_script("arguments[0].click();", gotoHome)

        print("=> Drug Details to Dashboard")

        time.sleep(2)


        myOffers = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/div/div/ul/li[5]/a")
        myOffers.click()
        print("=> My Offer List")

        time.sleep(10)
