# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from PO.login_page import Login
from Data.driver_desired_caps import *


class TestCaseLogin(unittest.TestCase):

    def setUp(self):
        print '执行登录setup'
        self.driver = Driver_Desired_Caps.driver

    def test_a_login(self):
        print '执行登录testcase'

        login = Login(self.driver)
        login.click_personal_icon()
        login.click_login_page()
        login.send_username()
        login.send_password()
        login.click_login_button()
        login.find_setting()

    def tearDown(self):
        # self.driver.quit()
        print '执行登录teardown'


if __name__ == '__main__':
    unittest.main()
