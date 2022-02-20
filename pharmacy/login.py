import time

class loginPage():

    def loginUser(self, driver):
        print("=> Register to Login")

        searchField = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[2]/p/a')
        searchField.click()
        time.sleep(1)

        print("==>> Entering credentials")

        email = driver.find_element_by_name('email')
        password = driver.find_element_by_name('Password')

        email.send_keys("test_store@gmail.com")
        password.send_keys("123456")
        time.sleep(1)

        print("==>> All fields filled")

        signFormBtn = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[2]/div[1]/div/form/button')

        signFormBtn.click()

        print("==>> Login successfully")

        time.sleep(5)