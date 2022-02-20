import time


class Add_License():
    import time

    def Add(self, driver):
        searchField = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/div/div/ul/li[4]/a/span')
        searchField.click()
        time.sleep(3)

        MLN = driver.find_element_by_name('MLN')
        drugName = driver.find_element_by_name('drugName')
        disease  = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[3]/div/div/form/div[3]/select/option[4]')
        drugType = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[3]/div/div/form/div[4]/select/option[3]')
        API      = driver.find_element_by_name('API')
        SSCR     = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[3]/div/div/form/div[6]/div/div/div/input[1]')
        licenseIssue = driver.find_element_by_name('licenseIssue')
        licenseExpiry = driver.find_element_by_name('licenseExpiry')
        licenseImg = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[3]/div/div/form/div[9]/div/label/input')
        drugImg = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[3]/div/div/form/div[10]/div/label/input')
        submit = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[3]/div/div/form/div[11]/div[2]/button')

        MLN.send_keys("Test License")
        drugName.send_keys("Test Medicine")
        disease.click()
        drugType.click()
        API.send_keys("Test ingredients")
        SSCR.click()
        licenseIssue.send_keys("08-02-2022")
        licenseExpiry.send_keys("08-02-2025")
        licenseImg.send_keys("F:\FYP 2021 Group\Last nd Final FPY\Medicens\process.pdf")
        drugImg.send_keys("F:\FYP 2021 Group\Last nd Final FPY\Medicens\Getz Pharma\Trevia-50.png")

        time.sleep(5)
        submit.click()


        time.sleep(20)

        driver.close()