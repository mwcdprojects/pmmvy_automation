import logging
import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import Select

from Reg.verhoeff import *


class aadhaar_validations(unittest.TestCase):
    def setUp(self):
        self.email = ""
        self.name = ""
        self.pwd = ""
        self.confirm_pwd = ""
        self.mobilenumber = ""
        self.dept = ""
        self.desig = ""
        self.contactaddr = ""
        self.Aadhaar_avaialbilty_data = ""
        self.url = "http://training9.pmmvy-cas.nic.in/BackOffice/UserAccount/Login"
        self.a = string.ascii_letters + string.digits
        self.id1 = ''.join(random.choice(string.ascii_letters) for i in range(4)) + ''.join(
            random.choice(string.digits) for i in range(4))
        self.id2 = ''.join(random.choice(string.ascii_letters) for i in range(4)) + ''.join(
            random.choice(string.digits) for i in range(4))
        self.accountno = ''.join(random.choice(string.digits) for i in range(18))
        self.health_id = "H" + ''.join(random.choice(string.ascii_letters) for i in range(4)) + ''.join(
            random.choice(string.digits) for i in range(4))
        self.aadhaar1 = VerhoeffChecksum().generateVerhoeff(
            ''.join(random.choice(string.digits) for i in range(1, 12)))
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        for i in range(20):
            if int(self.aadhaar1[0]) == 0:
                self.aadhaar1 = VerhoeffChecksum().generateVerhoeff(
                    ''.join(random.choice(string.digits) for i in range(1, 12)))
            else:
                break
        self.aadhaar2 = VerhoeffChecksum().generateVerhoeff(
            ''.join(random.choice(string.digits) for i in range(1, 12)))
        for i in range(20):
            if int(self.aadhaar2[0]) == 0:
                self.aadhaar2 = VerhoeffChecksum().generateVerhoeff(
                    ''.join(random.choice(string.digits) for i in range(1, 12)))
            else:
                break
        self.driver = webdriver.Chrome("C:\\Users\\munarayanan\\Downloads\\chromedriver_win32\\chromedriver.exe")

    def test_01_aadhaar_validations(self):
        # Login
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        print("Title: {}".format(self.driver.title))
        self.driver.find_element_by_id("Email").click()
        self.driver.find_element_by_id("Email").send_keys("testautomation123@mailinator.com")
        print("Email Entered")
        self.driver.find_element_by_id("password").click()
        self.driver.find_element_by_id("password").send_keys('P@ssw0rd')
        print("Password Entered")
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="btnNewbeneficiary"]').click()
        time.sleep(3)
        # Registration date
        self.driver.find_element_by_xpath('//*[@id="dpicker1"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[1]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[6]/a').click()
        time.sleep(3)
        print("Registration Date => ", self.driver.find_element_by_xpath(
            "//input[@id='dpicker1']").get_attribute("value"))
        # No of children
        no_of_children = self.driver.find_elements_by_xpath('//*[@id="NoOfChildren"]')
        no_of_children[0].click()

        # Does benficiary have Aadhaar -'Yes'
        Aadhaar_avaialbilty_data = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/form/div[6]/div/div[1]/div[1]/div[1]/input[1]")
        time.sleep(3)
        # print(Aadhaar_avaialbilty_data[0].get_attribute('value'))
        # Aadhaar_avaialbilty_data.click()

        # Aadhaar number
        self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').click()
        aadno = VerhoeffChecksum().generateVerhoeff(
            ''.join(random.choice(string.digits) for i in range(1, 12)))

        for i in range(20):
            if int(aadno[0]) == 0:
                aadno = VerhoeffChecksum().generateVerhoeff(
                    ''.join(random.choice(string.digits) for i in range(1, 12)))
            else:
                break



        print ("Enter Aadhaar with trailing spaces")
        self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').clear()
        self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').send_keys(aadno+"    ")
        print("Beneficiary's aadhaar: {}".format(aadno+"    "))
        # Name  in AAdhaar
        self.driver.find_element_by_xpath('//*[@id="BenAadhaarCheck"]').click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath(
            "//span[@id='spnAadhar']").text == 'The entered Aadhaar Number is invalid. Please enter again', "Aadhaar validation failed"


        print ("Enter Aadhaar with leading spaces")
        self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').clear()
        self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').send_keys("    "+aadno)
        print("Beneficiary's aadhaar: {}".format("    "+aadno))
        # Name  in AAdhaar
        self.driver.find_element_by_xpath('//*[@id="BenAadhaarCheck"]').click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath(
            "//span[@id='spnAadhar']").text == 'The entered Aadhaar Number is invalid. Please enter again', "Aadhaar validation failed"

        print ("Enter Aadhaar with  spaces between numbers")
        self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').clear()
        self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').send_keys(aadno[:3]+"  "+aadno[3:])
        print("Beneficiary's aadhaar: {}".format(aadno[:3]+"  "+aadno[3:]))
        # Name  in AAdhaar
        self.driver.find_element_by_xpath('//*[@id="BenAadhaarCheck"]').click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath(
            "//span[@id='spnAadhar']").text == 'The entered Aadhaar Number is invalid. Please enter again', "Aadhaar validation failed"



        print ("Enter Aadhaar with less than 12 digits")
        self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').clear()
        self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').send_keys(aadno[1:])
        print("Beneficiary's aadhaar: {}".format(aadno[1:]))
        # Name  in AAdhaar
        self.driver.find_element_by_xpath('//*[@id="BenAadhaarCheck"]').click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath(
            "//span[@id='spnAadhar']").text == 'The entered Aadhaar Number is invalid. Please enter again', "Aadhaar validation failed"


        print ("Enter Aadhaar with greater than 12 digits")
        self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').clear()
        self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').send_keys(aadno+"22")
        print("Beneficiary's aadhaar: {}".format(aadno+"22"))
        # Name  in AAdhaar
        self.driver.find_element_by_xpath('//*[@id="BenAadhaarCheck"]').click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath(
            "//span[@id='spnAadhar']").text == 'The entered Aadhaar Number is invalid. Please enter again', "Aadhaar validation failed"



        print ("Entering valid aadhaar")
        self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').clear()
        self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').send_keys(aadno)
        print("Beneficiary's aadhaar: {}".format(aadno))
        # Name  in AAdhaar
        self.driver.find_element_by_xpath('//*[@id="BenAadhaarCheck"]').click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath(
            "//label[@id='lblBenAadharStatus']").text == 'Aadhaar is allowed for Registration', "Aadhaar validation failed"



        # Does Husband have aadhar card 'Yes'
        print ("Aadhaar - Yes")
        Father_Aadhaar_data = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/form/div[6]/div/div[2]/div[1]/div[1]/input[1]')
        time.sleep(3)
        #Father_Aadhaar_data.click()
        self.driver.find_element_by_xpath('//*[@id="txtFNameAsInAadhaar"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtFNameAsInAadhaar"]').send_keys('Akash Hebbar')

        haadno = VerhoeffChecksum().generateVerhoeff(
            ''.join(random.choice(string.digits) for i in range(1, 12)))
        print("Father's aadhaar: {}".format(haadno))
        for i in range(20):
            if int(haadno[0]) == 0:
                haadno = VerhoeffChecksum().generateVerhoeff(
                    ''.join(random.choice(string.digits) for i in range(1, 12)))
            else:
                break


        print ("Enter Aadhaar with trailing spaces")
        self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').clear()
        self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').send_keys(haadno+"    ")
        print("Beneficiary's aadhaar: {}".format(haadno+"    "))
        # Name  in AAdhaar
        self.driver.find_element_by_xpath('//*[@id="HusbandAadhaarCheck"]').click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath(
            "//span[@id='spnFAadhar']").text == 'The entered Aadhaar Number is invalid. Please enter again', "Aadhaar validation failed"


        print ("Enter Aadhaar with leading spaces")
        self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').clear()
        self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').send_keys("    "+haadno)
        print("Beneficiary's aadhaar: {}".format("    "+haadno))
        # Name  in AAdhaar
        self.driver.find_element_by_xpath('//*[@id="HusbandAadhaarCheck"]').click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath(
            "//span[@id='spnFAadhar']").text == 'The entered Aadhaar Number is invalid. Please enter again', "Aadhaar validation failed"

        print ("Enter Aadhaar with  spaces between numbers")
        self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').clear()
        self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').send_keys(haadno[:3]+"  "+haadno[3:])
        print("Beneficiary's aadhaar: {}".format(haadno[:3]+"  "+haadno[3:]))
        # Name  in AAdhaar
        self.driver.find_element_by_xpath('//*[@id="HusbandAadhaarCheck"]').click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath(
            "//span[@id='spnFAadhar']").text == 'The entered Aadhaar Number is invalid. Please enter again', "Aadhaar validation failed"



        print ("Enter Aadhaar with less than 12 digits")
        self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').clear()
        self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').send_keys(haadno[1:])
        print("Beneficiary's aadhaar: {}".format(haadno[1:]))
        # Name  in AAdhaar
        self.driver.find_element_by_xpath('//*[@id="HusbandAadhaarCheck"]').click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath(
            "//span[@id='spnFAadhar']").text == 'The entered Aadhaar Number is invalid. Please enter again', "Aadhaar validation failed"


        print ("Enter Aadhaar with greater than 12 digits")
        self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').clear()
        self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').send_keys(haadno+"22")
        print("Beneficiary's aadhaar: {}".format(haadno+"22"))
        # Name  in AAdhaar
        self.driver.find_element_by_xpath('//*[@id="HusbandAadhaarCheck"]').click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath(
            "//span[@id='spnFAadhar']").text == 'The entered Aadhaar Number is invalid. Please enter again', "Aadhaar validation failed"

        print ("Entering valid Aadhaar for Husband")
        self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').clear()
        self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').send_keys(haadno)
        self.driver.find_element_by_xpath('//*[@id="HusbandAadhaarCheck"]').click()
        assert self.driver.find_element_by_xpath(
            "//label[@id='lblHusbandAadharStatus']").text == 'Aadhaar is allowed for Registration', "Aadhaar validation failed"

        print ("Tests Passed")

def tearDown(self):
    if self.driver.title == "PRADHAN MANTRI MATRU VANDANA YOJANA":
        self.driver.quit()
    else:
        time.sleep(3)
        self.driver.find_element_by_xpath("//a[@class='dropdown']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@id='btnlogout']").click()
        time.sleep(1)
        self.assertIn("PRADHAN MANTRI MATRU VANDANA YOJANA", self.driver.title)
        print(self.driver.title)
        print("User Logged out Successfully")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
