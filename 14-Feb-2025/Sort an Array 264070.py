# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        maximum = max(nums)
        minimum = abs(min(nums))

        # create the counting space with the offset
        count = [0] * (maximum + minimum + 1) 
        for num in nums:
            count[num + minimum] += 1
        
        target = 0
        for idx, val in enumerate(count):
            for i in range(val):
                nums[target] = idx - minimum
                target += 1
        
        return nums