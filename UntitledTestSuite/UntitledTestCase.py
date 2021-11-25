# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

    
class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path=r'c:\Users\User\AppData\Local\Programs\ChromeDriver\chromedriver.exe')
        self.wd.implicitly_wait(30)

    def pr(self):
        print("Whooo")

    def test_untitled_test_case(self):
        wd = self.wd

        wd.get("http://localhost/addressbook/group.php")
        # open home page
        print("Chrome is up {}".format(wd.current_url))
         # wd.find_element_by_xpath("//input[@value='Login']").click()
        # login
        username = wd.find_element_by_name('user')
        username.send_keys('admin')
        username = wd.find_element_by_name('pass')
        username.send_keys('secret')



        wd.find_element_by_xpath("//input[@value='Login']").click()
        # open groups
        wd.find_element_by_name("new").click()
        # init group creation
        wd.find_element_by_name("group_name").click()
        # fill group firm
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("sldkfsdlfjnadsflkvdhfhf")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(";dsfmdf;lvmdzfvfhfh")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("fjjf")
        # submit group creation
        wd.find_element_by_name("submit").click()
        # return to groups page
        wd.find_element_by_link_text("group page").click()
        #logout
        wd.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    


    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()

