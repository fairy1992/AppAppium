# -*-coding: utf-8 -*-

import unittest
from TestCase.test_case_login import TestCaseLogin
from TestCase.test_case_home_search import TestCaseHomeSearch

# test_case_path = "/Users/Fairy/PycharmProjects/AppAppium/TestCase"
test_case_path = "..//AppAppium/TestCase"


def create_suite():
    uit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_case_path, pattern="test_*.py", top_level_dir= None)
    for tes_suite in discover:
        print(tes_suite)
        for test_case in tes_suite:
            uit.addTest(test_case)
    return uit


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(TestCaseLogin("test_a_login"))
    # suite.addTest(TestCaseHomeSearch('test_b_home_page_search'))

    suite = create_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
