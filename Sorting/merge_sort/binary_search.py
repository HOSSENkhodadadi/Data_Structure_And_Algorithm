from merge_sort import Sorting
import random
class Search:
    def binary_search(self, arr: list[int], x: int, low: int, high: int)-> int:
        if low  == high: 
            if arr[low] == x:
                return arr[low]
            else:
                return -1
        if low < high: 
            mid = (high + low)//2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self.binary_search(arr, x, low, mid -1)
            else:
                return self.binary_search(arr, x, mid + 1, high) 
        else:
            return -1
        

# arr = [random.randint(20, 100) for _ in range (10)]
arr = [i for i in range(10)]
arr = arr[::-1]
print('arr itself:', arr)
sort1 = Sorting()
sort1.merge_sort(arr, 0, len(arr) - 1)
print("sorted_array: ",arr)

search1 = Search()
print(search1.binary_search(arr, 5, 0, len(arr)-1))

        


