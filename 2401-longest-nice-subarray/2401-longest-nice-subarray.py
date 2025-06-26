class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        longest = 0
        cur = 0
        left = 0

        for right in range(length):
            while cur & nums[right]:
                cur = cur ^ nums[left]
                left += 1
            longest = max(longest, right - left + 1)
            cur = cur ^ nums[right]

        return longest
            