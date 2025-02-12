# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        res = []
        nums.sort()

        for i in range(length):
            if nums[i] == target:
                res.append(i)
        
        return res

        