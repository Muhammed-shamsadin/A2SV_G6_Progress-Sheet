# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref_count = defaultdict(int)
        pref_count[0] = 1
        curr_sum = 0
        total = 0

        for num in nums:
            curr_sum = curr_sum + num

            if curr_sum - k in pref_count:
                total += pref_count[curr_sum - k]

            pref_count[curr_sum] += 1
        
        return total