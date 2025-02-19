# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref_count = defaultdict(int)
        pref_count[0] = 1
        result = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            check = curr_sum % k

            if check in pref_count:
                result += pref_count[check]
            
            pref_count[check] += 1
        
        return result