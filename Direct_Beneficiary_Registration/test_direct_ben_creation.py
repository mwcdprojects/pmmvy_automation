import logging
import time
import unittest
import re
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from pathlib import Path
from Reg.verhoeff import *


class Direct_Ben_Reg(unittest.TestCase):
    def setUp(self):
        self.email = ""
        self.name = ""
        self.pwd = ""
        self.confirm_pwd = ""
        self.mobilenumber = str(random.randrange(1000000000, 9999999999))
        self.dept = ""
        self.desig = ""
        self.contactaddr = ""
        self.Aadhaar_avaialbilty_data = ""
        self.url = "http://training9.pmmvy-cas.nic.in/public/BeneficiaryUserAccount/login"
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

        self.driver2 = webdriver.Chrome(
            str(Path(__file__).parents[3]) + "\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.driver = webdriver.Chrome(
            str(Path(__file__).parents[3]) + "\\Downloads\\chromedriver_win32\\chromedriver.exe")

    def test_01_Register_new_user(self):
        # Login
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        main_window = self.driver.current_window_handle
        self.driver.switch_to_window(main_window)
        print("Title: {}".format(self.driver.title))
        self.driver.find_element_by_link_text("Click Here").click()
        time.sleep(3)
        print("Title: {}".format(self.driver.title))
        print("Enter Name of the Beneficiary")
        email = "test_automation" + str(random.randrange(100, 10000)) + "@mailinator.com"
        self.driver.find_element_by_id("FirstName").send_keys("Ramya")
        phno = self.mobilenumber
        print("Enter Phonenumber: {}".format(phno))
        self.driver.find_element_by_id("PhoneNo").send_keys(phno)
        print("Enter EmailId: {}".format(email))
        self.driver.find_element_by_id("EmailID").send_keys(email)
        print("Email Entered")
        time.sleep(3)
        self.driver.find_element_by_id("sendOTP").click()
        time.sleep(3)
        otptext = self.driver.switch_to_alert().text
        self.driver.switch_to_alert().accept()
        assert otptext == "OPT sent to your Email"
        print("Open mailinator in another window")
        window2 = self.driver2.get('http://www.mailinator.com/')
        self.driver2.maximize_window()
        # for i in range(3):
        #    self.driver.refresh()
        otp_window = self.driver2.window_handles[0]
        self.driver2.switch_to_window(otp_window)
        self.driver2.find_element_by_id("addOverlay").send_keys(email)
        time.sleep(2)
        self.driver2.find_element_by_id("go-to-public").click()
        time.sleep(5)
        self.driver2.find_element_by_partial_link_text("PMMVY - OTP for Registration").click()
        time.sleep(3)
        self.driver2.switch_to_frame('msg_body')
        otptext = self.driver2.find_element_by_tag_name('body').text
        pattern = r'\d'
        otpnumber = "".join(re.findall(pattern, otptext))
        print("Activate Benieficiary Registration window")
        self.driver.switch_to_window(main_window)
        print("Enter OTP number")
        self.driver.find_element_by_id("EmailOTP").send_keys(otpnumber)
        self.driver.find_element_by_id('ValidateOTP').click()
        time.sleep(2)
        alerttext = self.driver.switch_to_alert().text
        assert alerttext == 'Your enterd Correct OTP', "OTP Failure"
        self.driver.switch_to_alert().accept()
        print("Enter Hint Question: {}".format("What is your school name"))
        self.driver.find_element_by_id("HintQuestion").send_keys("What is your school name")
        print("Enter Hint Answer")
        self.driver.find_element_by_id("HintAnswer").send_keys("SCS")

        self.driver.find_element_by_name("Password").send_keys('P@ssw0rd')
        print("Password Entered")
        self.driver.find_element_by_name("ConfirmPassword").send_keys('P@ssw0rd')
        print("Confirm Password Entered")

        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(5)
        print(self.driver.title)
        successtext = self.driver.find_elements_by_tag_name('h4')[0].text
        print(successtext)
        assert successtext == 'User Saved Successfully', "Registration Failed."
        print ("New User: {}".format(email))
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
