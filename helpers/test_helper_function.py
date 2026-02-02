import unittest
from helper_functions import _load_new_with_0, is_monotonic

class TestHelper(unittest.TestCase):

    def test_load_0(self):
        test_case_1 = [[1, 2, 3, 4]]
        test_case_2 = [[1, 2, 3, 4], [1, 2, 3, 4]]
        _load_new_with_0(test_case_1, len(test_case_1[0]))
        _load_new_with_0(test_case_2, len(test_case_2[0]))
        
        self.assertEqual(test_case_1, [[1, 2, 3, 4],[0, 0, 0 ,0]])
        self.assertEqual(test_case_2, [[1, 2, 3, 4],[1, 2, 3, 4], [0, 0, 0, 0]])

    
    def test_is_monotonic(self):
        test_case_1 = [3, 6, 7, 8, 9]
        test_case_2 = [2, 1, 0]
        test_case_3 = [1, 2, 2, 3]
        self.assertTrue(is_monotonic(test_case_1))
        self.assertFalse(is_monotonic(test_case_2))
        self.assertFalse(is_monotonic(test_case_3))


if __name__ == '__main__':
    unittest.main()