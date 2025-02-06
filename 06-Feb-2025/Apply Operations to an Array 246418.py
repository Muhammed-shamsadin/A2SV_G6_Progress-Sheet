# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # scene

        arr = []

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
                i += 1
        
        for num in nums:
            if num != 0:
                arr.append(num)

        zeros_arr = [0] * (len(nums) - len(arr)) 
        arr.extend(zeros_arr)

        return arr                
            