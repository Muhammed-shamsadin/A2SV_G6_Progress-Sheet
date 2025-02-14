# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        length = len(nums)
        left, right = 0, 0
        maximum_len = 0

        while right < length:
            if nums[right] == 0:
                k -= 1
            
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            
            maximum_len = max(maximum_len, right - left + 1)
            right += 1

        return maximum_len
