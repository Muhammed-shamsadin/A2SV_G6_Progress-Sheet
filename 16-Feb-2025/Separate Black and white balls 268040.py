# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        '''
        Approach: We keep the count of the black balls and if a white ball appears after the black ball 
                  that means we need to swap the black ball with the white ball.
                  More of it is about counting the possibilities of swapping.
        '''

        swap, black = 0, 0

        for char in s:
            if char == "0":
                swap += black
            else:
                black += 1
        
        return swap