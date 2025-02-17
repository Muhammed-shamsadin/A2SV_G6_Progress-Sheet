# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        '''
            scene
        '''
        n = len(nums)
        s = []
        for num in nums:
            s.append(str(num))
        
        # bubble sort the numbers
        for i in range(n):
            for j in range(n - i - 1):
                if s[j] + s[j+1] < s[j+1] + s[j]:
                    s[j], s[j+1] = s[j+1], s[j]                
        
        if int(''.join(s)) == 0:
            return "0"

        return ''.join(s)
