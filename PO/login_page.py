#coding=utf-8


from appium import webdriver
from selenium.webdriver.common.by import By

import base_pages
from Data.element_recourse import *
import time


class Login(base_pages.Base):

    # get = BasePages.Base()

    def click_personal_icon(self):
        time.sleep(5)
        self.click_button(ElementRecourse.personal)

    def click_login_page(self):
        self.click_button(ElementRecourse.loginpage)

    def send_username(self):
        self.send_keys(ElementRecourse.username, ElementRecourse.username_value)

    def send_password(self):
        self.send_keys(ElementRecourse.password, ElementRecourse.password_value)

    def click_login_button(self):
        self.click_button(ElementRecourse.login)

    def find_setting(self):
        self.find_element(ElementRecourse.setting)





