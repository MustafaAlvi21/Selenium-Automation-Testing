import time

class registerPage():

    def registerUser(self, driver):
        print("=> Home Page to Register")

        searchField = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/header/section/div/div[1]/div[4]/a')
        searchField.click()
        time.sleep(2)

        print("=> Start registration")
        businessName  = driver.find_element_by_name('businessName')
        role = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[1]/div/form/div[2]/div/select/option[4]')
        Primary_Email = driver.find_element_by_name('Primary_Email')
        Password = driver.find_element_by_name('Password')
        wallet = driver.find_element_by_name('wallet')
        Contact_Primary = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[1]/div/form/div[6]/div/input[2]')
        Contact_Secondary = driver.find_element_by_name('Contact_Secondary')
        Company_Address_Line_1 = driver.find_element_by_name('Company_Address_Line_1')
        City = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[1]/div/form/div[10]/div/select/option[2]')

        businessName.send_keys('Test Pharmacy')
        role.click()
        Primary_Email.send_keys('test_store@gmail.com')
        Password.send_keys('123456')
        wallet.send_keys('0x9FaF27967bF14fba1a7A58629e0AB7394ed9f25p')
        Contact_Primary.send_keys('3438338355')
        Contact_Secondary.send_keys('3439339356')
        Company_Address_Line_1.send_keys('Company_Address_Line_1')
        City.click()

        print("==>> All fields filled")
        time.sleep(1)

        Submit = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[1]/div/form/button')


        Submit.click()
        print("==>> Registered succesfully")

        time.sleep(5)