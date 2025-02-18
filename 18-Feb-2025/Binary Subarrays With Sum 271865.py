# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref_count = defaultdict(int)
        pref_count[0] = 1
        result = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            check = curr_sum - goal

            if check in pref_count:
                result += pref_count[check]
            
            pref_count[curr_sum] += 1

        return result