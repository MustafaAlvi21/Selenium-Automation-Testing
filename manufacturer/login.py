import time


class loginPage():
    import time

    def loginUser(self, driver):
        searchField = driver.find_element_by_xpath('//*[@id="navbarNavAltMarkup"]/a')
        searchField.click()
        time.sleep(1)

        email = driver.find_element_by_name('email')
        password = driver.find_element_by_name('Password')

        email.send_keys("getzpharma@gmail.com")
        password.send_keys("123456")
        time.sleep(1)

        signFormBtn = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div[1]/div/form/button')

        signFormBtn.click()

        time.sleep(5)