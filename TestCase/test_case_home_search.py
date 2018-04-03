# -*- coding:UTF-8 -*-

import unittest
from PO.home_search import HomeSearch

from Data.driver_desired_caps import *


class TestCaseHomeSearch(unittest.TestCase):
    def setUp(self):
        print '执行搜索setup'
        self.driver = Driver_Desired_Caps.driver

    def test_b_home_page_search(self):
        print '执行搜索testcase'
        home_search = HomeSearch(self.driver)
        home_search.click_home_page()
        home_search.click_home_page_search()
        home_search.input_search_content()
        home_search.click_search_tip()
        home_search.search_success_judge()
        home_search.search_result_back()
        print "1"
        home_search.search_back()
        print '2'
        home_search.search_back()

    def tearDown(self):
        print "'执行搜索teardown'"
        # self.driver.quit()

if __name__ == '__main__':
    unittest.main()
