#!C:\Python27\python.exe

"""
Enter a beneficiary using non aadhaar as ID proof for both beneficiary & husband. Apply for 2nd claim	Beneficiary form should be sent for SO approval. All the forms should not be editable
withdraw the beneficiary registration form	Beneficiary registration form, 1st & 2nd claim forms should be editable. Registration form should be removed from 'Beneficiary Approval' tab of SO user
click on Edit and change the MCP card date (select MCP card date 150 days after LMP card date to make it ineligible i e MCP card date - LMP date < 150 days)	Should be able to edit the MCP card date and after submission, form should be sent for SO approval and 1st claim should be marked as ineligible. 2nd claim will remain in editable mode until DEO resubmita claim form

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


class withdrawal_13(unittest.TestCase):
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

    def test_13_Reg_1st_2nd_claim(self):
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
        self.driver.find_element_by_xpath('//*[@id="CategoryName"]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="HealthId"]').send_keys(self.id2)

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
        print ("Verify that it is sent for SO Approval and form is not editable")

        assert self.driver.find_element_by_xpath("//table[@class='table table-bordered']/tbody/tr/td[5]").text == 'Pending SO Approval'
        assert self.driver.find_element_by_xpath("//table[@class='table table-bordered']/tbody/tr[2]/td[5]").text == 'Registration Pending SO Approval'
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
        print ("Withdraw the Beneficiary Registration")

        print ("Edit the details and submit")
        print ("Enter AlternateID for both husband and beneficiary")
        time.sleep(2)
        self.driver.find_element_by_link_text('WITHDRAW').click()
        print (self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        print (self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        assert self.driver.find_element_by_xpath("//table[@class='table table-bordered']/tbody/tr/td[5]").text == 'Withdrawn by DEO'
        assert self.driver.find_element_by_xpath("//table[@class='table table-bordered']/tbody/tr[2]/td[5]").text == 'Registration Withdrawn by DEO'
        self.driver.find_element_by_link_text("EDIT").click()
        print("Editing ben details and edit MCP 150 days after LMP date")
        self.driver.find_element_by_xpath('//*[@id="dpicker3"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[9]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[7]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[6]/a').click()
        time.sleep(3)
        print("Date of MCP => ", self.driver.find_element_by_xpath(
            "//input[@id='dpicker3']").get_attribute("value"))
        time.sleep(2)
        self.driver.find_element_by_id('btnVerify').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[1]').click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/h5')
        time.sleep(3)

        assert self.driver.find_element_by_xpath(
            "//table[@class='table table-bordered']/tbody/tr/td[5]").text == 'Pending SO Approval'
        assert self.driver.find_element_by_xpath(
            "//table[@class='table table-bordered']/tbody/tr[2]/td[5]").text == 'Ineligible Case'


        print(self.driver.find_element_by_xpath("//table[@class='table table-bordered']/tbody/tr/td[5]").text)
        print(self.driver.find_element_by_xpath("//table[@class='table table-bordered']/tbody/tr[2]/td[5]").text)

        print ("Verify if second claim form is editable")
        assert self.driver.find_element_by_xpath("//table[@class='table table-bordered']/tbody/tr[3]/td[7]").text == 'EDIT'
        print(self.driver.find_element_by_xpath("//table[@class='table table-bordered']/tbody/tr[3]/td[7]").text)
        assert self.driver.find_elements_by_link_text("EDIT")[0].is_displayed() == True


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
    suite = unittest.TestLoader().loadTestsFromTestCase(withdrawal_13)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    # print "Testresult" , testResult , type(testResult) , dir(testResult)
    print("fails", len(testResult.failures))
    if len(testResult.failures) > 0:
        sys.exit(1)
