# coding=utf-8


from appium import webdriver
from selenium.webdriver.common.by import By

import base_pages
from Data.element_recourse import *


class CustomOrder(base_pages.Base):

    def click_classify(self):
        self.click_button(ElementRecourse.classify)

    def click_classify_product_pic(self):
        self.click_button(ElementRecourse.product_pic)

    def click_product_pic(self):
        self.click_button(ElementRecourse.search_result_pic)

    def buy_product(self):
        self.click_button(ElementRecourse.buy_now)
        self.click_button(ElementRecourse.buy)

    def confirm_order(self):
        self.click_button(ElementRecourse.confirm_order)

    def judge_confirm_order(self):
        self.find_element(ElementRecourse.order_success_tip)
