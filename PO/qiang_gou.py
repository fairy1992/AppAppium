# coding=utf-8


from appium import webdriver
from selenium.webdriver.common.by import By

import base_pages
from Data.element_recourse import *


class QiangGou(base_pages.Base):

    def click_home_page(self):
        self.click_button(ElementRecourse.homepage)

    def click_qianggou_tab(self):
        self.click_button(ElementRecourse.home_bar_xianshigou)

    def open_qianggou_product(self):
        self.click_button(ElementRecourse.qiang_gou_product_list)

    def qiang_gou(self):
        self.click_button(ElementRecourse.qiang_gou_btn)

