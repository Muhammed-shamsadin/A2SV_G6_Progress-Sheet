# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        tot_even = 0
        for num in nums:
            if num % 2 == 0:
                tot_even += num
        
        new_sum = 0
        for val, index in queries:
            if nums[index] % 2 == 0:
                tot_even -= nums[index]

            new_sum = nums[index] + val
            if new_sum % 2 == 0:
                tot_even += new_sum
            
            nums[index] = new_sum

            res.append(tot_even)
        
        return res