# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from PO.qiang_gou import QiangGou
from Data.driver_desired_caps import *


class TestCaseQiangGou(unittest.TestCase):

    def setUp(self):
        print '执行抢购setup'
        self.driver = Driver_Desired_Caps.driver

    def test_qianggou(self):
        print '执行抢购testcase'
        qianggou = QiangGou(self.driver)
        qianggou.click_home_page()
        qianggou.click_qianggou_tab()
        qianggou.open_qianggou_product()
        qianggou.qiang_gou()

    def tearDown(self):
        # self.driver.quit()
        print '执行抢购teardown'


if __name__ == '__main__':
    unittest.main()
