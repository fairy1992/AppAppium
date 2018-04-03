# -*- coding:UTF-8 -*-

import unittest
from PO.custom_order import CustomOrder

from Data.driver_desired_caps import *


class TestCaseCustomOrder(unittest.TestCase):
    def setUp(self):
        print '执行下单setup'
        self.driver = Driver_Desired_Caps.driver

    def test_custom_order(self):
        custom_order = CustomOrder(self.driver)
        custom_order.click_classify()
        custom_order.click_classify_product_pic()
        custom_order.click_product_pic()
        custom_order.buy_product()
        custom_order.confirm_order()
        custom_order.judge_confirm_order()

    def tearDown(self):
        print "'执行搜索teardown'"
        # self.driver.quit()

if __name__ == '__main__':
    unittest.main()
