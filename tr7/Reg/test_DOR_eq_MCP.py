import logging
import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import Select

from Reg.verhoeff import *


class DORMCP(unittest.TestCase):
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
        self.url = "http://training7.pmmvy-cas.nic.in/BackOffice/UserAccount/Login"
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

    def test_01_DOREQMCP(self):
        # Login
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        print("Title: {}".format(self.driver.title))
        self.driver.find_element_by_id("Email").click()
        self.driver.find_element_by_id("Email").send_keys("deo_fanda@mailinator.com")
        print("Email Entered")
        self.driver.find_element_by_id("password").click()
        self.driver.find_element_by_id("password").send_keys('Welcome@123')
        print("Password Entered")
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="btnNewbeneficiary"]').click()
        time.sleep(3)
        # Registration date
        self.driver.find_element_by_xpath('//*[@id="dpicker1"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[1]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[4]/a').click()
        print("Registration Date: {}".format(
            self.driver.find_element_by_xpath("//input[@id='dpicker1']").get_attribute("value")))
        # No of children
        self.no_of_children = self.driver.find_elements_by_xpath('//*[@id="NoOfChildren"]')
        self.no_of_children[0].click()

        self.Aadhaar_avaialbilty_data = self.driver.find_elements_by_xpath("//input[@id='BeneficiaryAadharExistVal']")
        time.sleep(3)

        self.Aadhaar_avaialbilty_data[3].click()
        print(self.Aadhaar_avaialbilty_data[3].get_attribute('value'))
        select = Select(self.driver.find_element_by_id('beneficiaryAltID'))
        select.select_by_value('5')

        self.driver.find_element_by_xpath('//*[@id="txtAlternateNumber"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtAlternateNumber"]').send_keys(self.id1)
        print ("Id: {}".format(self.id1))
        self.driver.find_element_by_xpath('//*[@id="NameAsInIDCard"]').click()
        self.driver.find_element_by_xpath('//*[@id="NameAsInIDCard"]').send_keys('Shanthala')

        # Does Husband have aadhar card 'No'

        self.Father_Aadhaar_data = self.driver.find_elements_by_xpath("//input[@id='FatherAadharExistVal']")
        time.sleep(3)

        self.Father_Aadhaar_data[3].click()
        print(self.Father_Aadhaar_data[3].get_attribute('value'))
        select = Select(self.driver.find_element_by_id('fatherAltID'))
        select.select_by_value('5')

        self.driver.find_element_by_xpath('//*[@id="txtFatherAlternateNumber"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtFatherAlternateNumber"]').send_keys(self.id2)
        print ("Id:{}".format(self.id2))
        self.driver.find_element_by_xpath('//*[@id="FNameAsInIDCard"]').send_keys('Shashikanth')
        self.driver.find_element_by_xpath('//*[@id="Phone"]').send_keys('9989009896')
        select1 = Select(self.driver.find_element_by_xpath('//*[@id="Category"]'))
        select1.select_by_index('3')
        self.driver.find_element_by_xpath('//*[@id="HealthId"]').send_keys(self.id2)

        # Date of LMP
        self.driver.find_element_by_xpath('//*[@id="dpicker2"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[6]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[1]/a').click()
        time.sleep(3)

        # Date of registration of MCP

        self.driver.find_element_by_xpath('//*[@id="dpicker3"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[6]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[1]/a').click()
        print("Date of Reg of MCP card at AWC/ Subcenter => ", self.driver.find_element_by_xpath(
            "//input[@id='dpicker3']").get_attribute("value"))
        # Present Address

        self.driver.find_element_by_xpath('//*[@id="AddressLine1"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine1"]').send_keys('801')

        self.driver.find_element_by_xpath('//*[@id="AddressLine2"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine2"]').send_keys('15th Cross')

        self.driver.find_element_by_xpath('//*[@id="AddressLine3"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine3"]').send_keys('Bull Temple Road')

        self.driver.find_element_by_xpath('//*[@id="AreaLocalitySector"]').click()
        self.driver.find_element_by_xpath('//*[@id="AreaLocalitySector"]').send_keys('Alankady')

        select = Select(self.driver.find_element_by_xpath('//*[@id="drpAnganvaadi"]'))
        ###Temp data
        select.select_by_index('6')
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').click()
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').send_keys('670648')

        # Account Details
        self.driver.find_element_by_xpath('//*[@id="Bank"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').send_keys('SBIN0005099')
        self.driver.find_element_by_xpath('//*[@id="ifscButton1"]').click()
        print(self.driver.find_element_by_xpath("//label[@id='lblStatus']").text)
        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').send_keys(self.accountno)

        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').send_keys('Shanthala')

        self.driver.find_element_by_xpath('//*[@id="btnVerify"]').click()

        # Submit

        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[1]').click()
        time.sleep(5)
        self.driver.switch_to.alert.accept()

        time.sleep(5)

        # To cancel
        # driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()

        # To check if the form is submitted
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/h5')
        assert element.text == 'The beneficiary application form is sent for approval'
        print(element.text)

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
