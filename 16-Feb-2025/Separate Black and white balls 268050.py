# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        '''
        Approach: Another approach was to have my right pointer searching for "0" and calculating the
                length between my left pointer where the "0" should be and where the position of 0 is, 
                to make a swap, doing the same for all "0" and adding to the min_steps. 
        '''
        length = len(s)
        distance = 0
        minimum_step = 0

        left = 0
        right = 0

        while right < length:
            if s[right] == '0':
                distance = right - left
                minimum_step += distance
                left += 1
            
            right += 1
        
        return minimum_step