import unittest
import random 
from insertion_sort import Sorting

class test_insertion_sort (unittest.TestCase):
    def sorting_test_1(self):
        arr1 = [x for x in range(20)]
        arr2 = arr1
        arr1 = arr1[::-1]
        sorted_arr1 = Sorting.insertion_sort(arr1)
        self.assertEqual(sorted_arr1, arr2)

    # def sorting_test_2(self):
    #     my_arr = [random.randint(20, 100) for _ in range(50)]
    #     sorted_my_arr = Sorting.insertion_sort(my_arr)
    #     self.assertEqual(sorted_my_arr, Sorting.anotherSorting)         



if __name__ == "__main__":
    unittest.main()

