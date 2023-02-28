import unittest

import unit_tests.my_test_test_1 as my_test_test_1

test_1 = my_test_test_1.TestTest1()
test_1.setUp()
test_1.test_convert_dashes()


if __name__ == "__main__":
  unittest.main()




