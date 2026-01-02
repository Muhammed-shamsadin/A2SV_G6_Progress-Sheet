class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        counter = Counter(nums)
        n = len(nums) // 2

        for num in nums:
            if counter[num] == n:
                return num
            