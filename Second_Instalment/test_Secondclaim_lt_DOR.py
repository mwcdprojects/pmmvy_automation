import logging
import time
import unittest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from Reg.verhoeff import *


class SecondclaimltDOR(unittest.TestCase):
    def setUp(self):
        self.email = ""
        self.name = ""
        self.pwd = ""
        self.confirm_pwd = ""
        self.mobilenumber = ""
        self.dept = ""
        self.desig = ""
        self.contactaddr = ""
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
        self.driver = webdriver.Chrome(str(Path(__file__).parents[4]) + "\\chromedriver_win32\\chromedriver.exe")

    def test_01_SecondclaimltDOR(self):
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
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[4]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[2]/a').click()
        time.sleep(3)
        print("Registration Date: {}".format(
            self.driver.find_element_by_xpath("//input[@id='dpicker1']").get_attribute("value")))
        # No of children
        no_of_children = self.driver.find_elements_by_xpath('//*[@id="NoOfChildren"]')
        no_of_children[0].click()

        # Does benficiary have Aadhaar -'No'
        Aadhaar_avaialbilty_data = self.driver.find_elements_by_xpath("//input[@id='BeneficiaryAadharExistVal']")
        time.sleep(3)

        Aadhaar_avaialbilty_data[3].click()
        print(Aadhaar_avaialbilty_data[3].get_attribute('value'))
        # Driving license

        select = Select(self.driver.find_element_by_id('beneficiaryAltID'))
        select.select_by_value('6')
        # Identity number
        self.driver.find_element_by_xpath('//*[@id="txtAlternateNumber"]').click()
        dlic = ''.join(random.choice('0123ABC') for i in range(10))
        self.driver.find_element_by_xpath('//*[@id="txtAlternateNumber"]').send_keys(dlic)
        print("Driving License: {}".format(dlic))

        # Name as in ID proof
        self.driver.find_element_by_xpath('//*[@id="NameAsInIDCard"]').click()
        self.driver.find_element_by_xpath('//*[@id="NameAsInIDCard"]').send_keys('Adithi')

        # Does Husband have aadhar card 'No'

        Father_Aadhaar_data = self.driver.find_elements_by_xpath("//input[@id='FatherAadharExistVal']")
        time.sleep(3)
        Father_Aadhaar_data[3].click()
        # Driving License
        select = Select(self.driver.find_element_by_id('fatherAltID'))
        select.select_by_value('6')
        # Husband's Identity number
        dlic = ''.join(random.choice('0123ABC') for i in range(10))
        self.driver.find_element_by_xpath('//*[@id="txtFatherAlternateNumber"]').send_keys(dlic)
        print("Driving License: {}".format(dlic))
        # Husband's name
        self.driver.find_element_by_xpath('//*[@id="FNameAsInIDCard"]').send_keys('Adarsh')

        # Phone number
        phone = ''.join(random.choice('0123456789') for i in range(10))
        self.driver.find_element_by_xpath('//*[@id="Phone"]').send_keys(phone)
        # Category Others
        select1 = Select(self.driver.find_element_by_xpath('//*[@id="Category"]'))
        select1.select_by_index('3')
        # Health id
        healthid = ''.join(random.choice('0123ABC') for i in range(7))
        self.driver.find_element_by_xpath('//*[@id="HealthId"]').send_keys(healthid)
        print("Healthid: {}".format(healthid))

        # Date of LMP
        self.driver.find_element_by_xpath('//*[@id="dpicker2"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[6]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[1]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[3]/a').click()
        time.sleep(3)
        print("Date of LMP => ", self.driver.find_element_by_xpath(
            "//input[@id='dpicker2']").get_attribute("value"))

        # Date of registration of MCP

        self.driver.find_element_by_xpath('//*[@id="dpicker3"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[6]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[6]/a').click()
        print("Date of Reg of MCP card at AWC/ Subcenter => ", self.driver.find_element_by_xpath(
            "//input[@id='dpicker3']").get_attribute("value"))
        # Present Address

        self.driver.find_element_by_xpath('//*[@id="AddressLine1"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine1"]').send_keys('110')
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="AddressLine2"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine2"]').send_keys('2nd Main')

        self.driver.find_element_by_xpath('//*[@id="AddressLine3"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine3"]').send_keys('Bull Temple Road')

        self.driver.find_element_by_xpath('//*[@id="AreaLocalitySector"]').click()
        self.driver.find_element_by_xpath('//*[@id="AreaLocalitySector"]').send_keys('Alankady')

        select = Select(self.driver.find_element_by_xpath('//*[@id="drpAnganvaadi"]'))
        # Temp data
        select.select_by_index('6')
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').click()
        pin = ''.join(random.choice('456789') for i in range(6))
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').send_keys(pin)

        # Account Details
        self.driver.find_element_by_xpath('//*[@id="Bank"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').send_keys('SBIN0005099')
        self.driver.find_element_by_xpath('//*[@id="ifscButton1"]').click()

        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').click()
        accno = ''.join(random.choice('0123456789') for i in range(14))
        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').send_keys(accno)

        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').send_keys('Adithi')

        self.driver.find_element_by_xpath('//*[@id="btnVerify"]').click()

        # Submit
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[1]').click()
        time.sleep(5)
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/h5')
        time.sleep(5)
        assert element.text == 'The beneficiary application form is sent for approval'
        print(element.text)

        # Second instalment details
        print("Second Instalment")
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[11]/div/div/div[1]/div/a[2]').click()
        # Date of Claim at the Field Functionary Centre
        self.driver.find_element_by_xpath('//*[@id="dpicker"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[1]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[3]/a').click()
        print("Date of Claim at the Field Functionary Centre => ", self.driver.find_element_by_xpath(
            "//input[@id='dpicker']").get_attribute("value"))
        # ANC Date
        self.driver.find_element_by_xpath('//*[@id="dpicker1"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[6]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[3]/a').click()
        print("ANC Date => ", self.driver.find_element_by_xpath(
            "//input[@id='dpicker1']").get_attribute("value"))

        # Was ANC recorded on MCP card?
        #ancrec = self.driver.find_elements_by_xpath('//*[@id="MCPCardANCValue"]')
        #ancrec[0].click()
        # Save
        self.driver.find_element_by_xpath('//*[@id="btnSave"]').click()
        self.driver.switch_to.alert.accept()
        # Assert for the message
        time.sleep(5)
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div[8]/div/span[3]/span')
        time.sleep(5)
        assert element.text == 'Claim date should not be less than Registration/First Instalment date. Please enter the correct date'
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
