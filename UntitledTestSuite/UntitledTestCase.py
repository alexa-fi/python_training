# -*- coding: utf-8 -*-
from selenium import webdriver
from group import Group
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
        self.open_home_page(wd)

        print("Chrome is up {}".format(wd.current_url))
         # wd.find_element_by_xpath("//input[@value='Login']").click()
        self.login(wd, username='admin', password='secret')
        self.open_groups(wd)
        self.create_group(wd, Group(name="sldkfsdlfjnadsflkvdhfhf", header=";dsfmdf;lvmdzfvfhfh", footer="fjjf"))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_untitled_test_case(self):
        wd = self.wd
        self.open_home_page(wd)

        print("Chrome is up {}".format(wd.current_url))
        # wd.find_element_by_xpath("//input[@value='Login']").click()
        self.login(wd, username='admin', password='secret')
        self.open_groups(wd)
        self.create_group(wd, Group(name=" ", header=" ", footer=" "))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wd):
        # return to groups page
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, group):
        # init group creation
        wd.find_element_by_name("group_name").click()
        # fill group firm
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def open_groups(self, wd):
        # open groups
        wd.find_element_by_name("new").click()

    def login(self, wd, username, password):
        # login
        user = wd.find_element_by_name('user')
        user.send_keys(username)
        passwd = wd.find_element_by_name('pass')
        passwd.send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/group.php")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    


    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()

