# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
        Approach: We will be using Dictionary (Hash map): this will help us have the constant space and 
        O(n) time
        '''
        check = defaultdict(int)
        for num in nums:
            check[num] += 1
        
        res = []

        for key, value in check.items():
            if value == 2:
                res.append(key)
        
        return res