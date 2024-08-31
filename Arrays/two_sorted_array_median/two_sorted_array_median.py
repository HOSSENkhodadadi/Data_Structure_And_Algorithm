class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        len1 = len (nums1)
        len2 = len (nums2)
        parity = (len1 + len2) % 2
        if len1 == 0:
            if len2 == 0:
                return 0.0
            elif parity == 0:
                return (nums2[len2//2]+ nums2[(len2//2)-1])/2
            else:
                return nums2[len2 // 2]  
        
        elif len2 == 0:
            if parity == 0:
                return (nums1[len1 // 2 - 1] + nums1[len1 // 2]) / 2
            else:
                return nums1[len1 // 2]   
            
        if parity == 0:
            counter = 0
            med1 = 0
            med2 = 0
            i = j = 0
            if nums1[0] <= nums2[0]:
                med2 =nums1[0]
                i = 1
            else:
                med2 = nums2[0]
                j = 1

            while counter < (len1 + len2)/2:
                counter = i + j
                if i == (len1):
                    med1 = med2 
                    med2 = nums2[j]
                    j += 1
                elif j == (len2):
                    med1 = med2
                    med2 = nums1[i]
                    i += 1
                
                elif nums1[i] <= nums2[j]:
                    med1 = med2
                    med2 = nums1[i]
                    i += 1 
                else:
                    med1 = med2
                    med2 = nums2[j]
                    j += 1
            return (med1 + med2)/2
        else:
            counter = 0
            i = j = 0
            median = 0
            while counter < ((len1 + len2 + 1)/2)-1:
                counter = i + j
                if i == (len1):
                    median = nums2[j]
                    j += 1

                elif j == (len2):
                    median = nums1[i]
                    i += 1

                elif nums1[i] <= nums2[j]:
                    median = nums1[i]
                    i += 1
                else:
                    median = nums2[j]
                    j += 1
            return median 


list1 = [6, 7]
list2 = [1,2, 3, 4]
sol1 = Solution()
median = sol1.findMedianSortedArrays(list1, list2)
print(median)