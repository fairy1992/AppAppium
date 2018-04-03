# coding=utf-8


from appium import webdriver
from selenium.webdriver.common.by import By

import base_pages
from Data.element_recourse import *


class HomeSearch(base_pages.Base):

    def click_home_page_search(self):
        self.click_button(ElementRecourse.home_page_search)

    def input_search_content(self):
        self.send_keys(ElementRecourse.search_text, 'iphone')

    def click_search_tip(self):
        self.click_button(ElementRecourse.search_input_tip)

    def search_success_judge(self):
        self.find_element(ElementRecourse.search_result_product_name)

    def click_home_page(self):
        self.click_button(ElementRecourse.homepage)

    def search_result_back(self):
        self.click_button(ElementRecourse.search_result_back)

    def search_back(self):
        self.click_button(ElementRecourse.search_back)

