#!C:\Python27\python.exe

"""
Enter a beneficiary using aadhaar as ID proof for both beneficiary & husband. Apply for 2nd claim	Beneficiary form should be sent for SO approval. All the forms should not be editable
Withdraw 2nd Claim	Only 2nd claim should be editable
Click on edit and change ANC date	Should be able to select ANC date and after submission the 2nd claim form should be non editable

"""
import sys
import collections
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import string
import random
from selenium.webdriver.support.ui import Select
from Reg.verhoeff import *


class withdrawal_10(unittest.TestCase):
    def setUp(self):
        self.email = ""
        self.name = ""
        self.pwd = ""
        self.confirm_pwd = ""
        self.mobilenumber = ""
        self.dept = ""
        self.desig = ""
        self.contactaddr = ""
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
        for i in range(20):
            if int(self.aadhaar1[0]) == 0:
                self.aadhaar1 = VerhoeffChecksum().generateVerhoeff(
                    ''.join(random.choice(string.digits) for i in range(1, 12)))
                print("Aadhaar1", self.aadhaar1)
            else:
                break
        self.aadhaar2 = VerhoeffChecksum().generateVerhoeff(
            ''.join(random.choice(string.digits) for i in range(1, 12)))
        for i in range(20):
            if int(self.aadhaar2[0]) == 0:
                self.aadhaar2 = VerhoeffChecksum().generateVerhoeff(
                    ''.join(random.choice(string.digits) for i in range(1, 12)))
                print("Aadhaar2", self.aadhaar2)
            else:
                break
        self.driver = webdriver.Chrome("C:\\Users\\munarayanan\\Downloads\\chromedriver_win32\\chromedriver.exe")

    def test_10_Reg_1st_2nd_claim_Edit_2nd_claim_withdrawal(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("http://training9.pmmvy-cas.nic.in/BackOffice/UserAccount/Login")
        time.sleep(3)

        # **************** #
        # Login validation #
        # **************** #

        emailid = self.driver.find_element_by_id("Email")
        emailid.send_keys("testautomation123@mailinator.com")
        time.sleep(3)
        print("Email entered")
        password = self.driver.find_element_by_id("password")
        password.send_keys("P@ssw0rd")
        print("Password entered")
        time.sleep(3)
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(4)
        # self.assertIn("Approval Queue - MWCD Backoffice", self.driver.title)
        print(self.driver.title)
        time.sleep(1)

        self.driver.find_element_by_id("btnNewbeneficiary").click()
        time.sleep(2)

        # Registration date
        self.driver.find_element_by_xpath('//*[@id="dpicker1"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[4]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[12]').click()
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

        # No id proof

        # select = Select(self.driver.find_element_by_id('beneficiaryAltID'))
        # select.select_by_value('6')
        # Identity number
        # self.driver.find_element_by_xpath('//*[@id="txtAlternateNumber"]').click()
        # dlic = ''.join(random.choice('0123ABC') for i in range(10))
        # self.driver.find_element_by_xpath('//*[@id="txtAlternateNumber"]').send_keys(dlic)

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
        self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').send_keys(self.aadhaar1)
        print("Beneficiary's aadhaar: {}".format(self.aadhaar1))
        # Name  in AAdhaar
        self.driver.find_element_by_xpath('//*[@id="txtNameAsInAadhar"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtNameAsInAadhar"]').send_keys('Raani')

        # Is the P.O/ Bank Account Aadhaar Seeded? Yes
        PO_bank_acc = self.driver.find_elements_by_xpath('//*[@id="IsBankAccountAadhaarSeededValue"]')
        time.sleep(3)
        PO_bank_acc[0].click()

        # Does Husband have aadhar card 'Yes'
        print("Aadhaar - Yes")
        Father_Aadhaar_data = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/form/div[6]/div/div[2]/div[1]/div[1]/input[1]')
        time.sleep(3)
        # Father_Aadhaar_data.click()
        self.driver.find_element_by_xpath('//*[@id="txtFNameAsInAadhaar"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtFNameAsInAadhaar"]').send_keys('Akash Hebbar')
        self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').click()
        aadno = VerhoeffChecksum().generateVerhoeff(
            ''.join(random.choice(string.digits) for i in range(1, 12)))
        print("Father's aadhaar: {}".format(self.aadhaar2))
        for i in range(20):
            if int(aadno[0]) == 0:
                aadno = VerhoeffChecksum().generateVerhoeff(
                    ''.join(random.choice(string.digits) for i in range(1, 12)))
            else:
                break
        self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').send_keys(self.aadhaar2)

        # Phone number
        phone = ''.join(random.choice('0123456789') for i in range(10))
        self.driver.find_element_by_xpath('//*[@id="Phone"]').send_keys(phone)
        # Category Others
        select1 = Select(self.driver.find_element_by_xpath('//*[@id="CategoryName"]'))
        select1.select_by_index('3')
        # Health id
        healthid = ''.join(random.choice('0123ABC') for i in range(7))
        self.driver.find_element_by_xpath('//*[@id="HealthId"]').send_keys(healthid)

        # Date of LMP
        self.driver.find_element_by_xpath('//*[@id="dpicker2"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[9]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[1]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[3]/a').click()
        time.sleep(3)
        print("Date of LMP => ", self.driver.find_element_by_xpath(
            "//input[@id='dpicker2']").get_attribute("value"))

        # Date of registration of MCP

        self.driver.find_element_by_xpath('//*[@id="dpicker3"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[9]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[6]/a').click()
        # Present Address
        print("Date of MCP => ", self.driver.find_element_by_xpath(
            "//input[@id='dpicker3']").get_attribute("value"))

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
        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').send_keys('Raani')

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
        time.sleep(5)
        print(element.text)
        print("Verify that it is sent for SO Approval and form is not editable")

        assert self.driver.find_element_by_xpath(
            "//table[@class='table table-bordered']/tbody/tr/td[5]").text == 'Pending SO Approval'
        assert self.driver.find_element_by_xpath(
            "//table[@class='table table-bordered']/tbody/tr[2]/td[5]").text == 'Registration Pending SO Approval'

        print ("Submit 2nd claim")
        # Second instalment details
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[11]/div/div/div[1]/div/a[2]').click()
        time.sleep(5)
        # Date of Claim at the Field Functionary Centre
        self.driver.find_element_by_xpath('//*[@id="dpicker"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[4]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[12]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[6]/a').click()
        time.sleep(5)
        print("Date of claim at Field Functionary Center => ", self.driver.find_element_by_xpath(
            "//input[@id='dpicker']").get_attribute("value"))
        # ANC Date
        self.driver.find_element_by_xpath('//*[@id="dpicker1"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[9]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[12]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[6]/a').click()
        time.sleep(5)
        print("ANC Date ", self.driver.find_element_by_xpath(
            "//input[@id='dpicker1']").get_attribute("value"))
        # Was ANC recorded on MCP card? Yes
        #ancrec = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div[10]/div/input[1]')
        # ancrec.click()
        # Save
        self.driver.find_element_by_xpath('//*[@id="btnSave"]').click()
        self.driver.switch_to.alert.accept()
        # Assert for the message
        time.sleep(5)
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/h5')
        time.sleep(5)
        assert element.text == 'The beneficiary application form is sent for approval'
        time.sleep(5)
        print(element.text)

        print("Withdraw the Beneficiary Registration")

        print("Edit the details and submit")
        print("Enter AlternateID for both husband and beneficiary")
        time.sleep(2)
        self.driver.find_elements_by_link_text('WITHDRAW')[2].click()
        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        print ("Edit 2nd claim and change ANC date")
        self.driver.find_element_by_link_text('EDIT').click()
        self.driver.find_element_by_xpath('//*[@id="dpicker1"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[9]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[12]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[4]/a').click()
        time.sleep(5)
        print("ANC Date ", self.driver.find_element_by_xpath(
            "//input[@id='dpicker1']").get_attribute("value"))
        self.driver.find_element_by_xpath('//*[@id="btnSave"]').click()
        self.driver.switch_to.alert.accept()
        # Assert for the message
        time.sleep(5)
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/h5')
        time.sleep(5)
        assert element.text == 'The beneficiary application form is sent for approval'
        time.sleep(5)
        print(element.text)

        assert self.driver.find_element_by_xpath(
            "//table[@class='table table-bordered']/tbody/tr/td[5]").text == 'Pending SO Approval'
        assert self.driver.find_element_by_xpath(
            "//table[@class='table table-bordered']/tbody/tr[2]/td[5]").text == 'Registration Pending SO Approval'
        assert self.driver.find_element_by_xpath(
            "//table[@class='table table-bordered']/tbody/tr[3]/td[5]").text == 'Registration Pending SO Approval'


        print(self.driver.find_element_by_xpath("//table[@class='table table-bordered']/tbody/tr/td[5]").text)
        print(self.driver.find_element_by_xpath("//table[@class='table table-bordered']/tbody/tr[2]/td[5]").text)
        print(self.driver.find_element_by_xpath("//table[@class='table table-bordered']/tbody/tr[3]/td[5]").text)



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


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(withdrawal_10)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    # print "Testresult" , testResult , type(testResult) , dir(testResult)
    print("fails", len(testResult.failures))
    if len(testResult.failures) > 0:
        sys.exit(1)
