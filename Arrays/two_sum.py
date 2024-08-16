class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        temp = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)) :
                if nums[i] + nums[j] == target:
                    temp.append((i,j)) 
        return temp
    
list1 = [x for x in range (10)]
target = 5
new_prob = Solution()
print(new_prob.twoSum(list1, target))