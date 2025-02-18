# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = float('-inf')

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += num
            max_sum = max(curr_sum, max_sum)
        
        return max_sum