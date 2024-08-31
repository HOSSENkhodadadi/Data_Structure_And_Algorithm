import unittest
from two_sorted_array_median import Solution

class TestTwoSortedArrayMedian(unittest.TestCase):
    def test_len1_plus_len2_even(self):
        list1 = [x for x in range(1, 5)]
        list2 = [y for y in range(5, 9)]
        median = Solution.findMedianSortedArrays(self, list1, list2)
        self.assertEqual(median, 4.5)
    def test_len1_plus_len2_odd(self):
        list1 = [x for x in range(1, 5)]
        list2 = [y for y in range(5, 10)]
        median = Solution.findMedianSortedArrays(self, list1, list2)
        self.assertEqual(median, 5)

if __name__ == '__main__':
    unittest.main()