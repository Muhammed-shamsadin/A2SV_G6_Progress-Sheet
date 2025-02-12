# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        rad = int(sqrt(c))
        left = 0
        right = rad

        while left <= right:
            operation = (left * left) + (right * right)

            if operation < c:
                left += 1
            elif operation > c:
                right -= 1
            else:
                return True

        
        return False