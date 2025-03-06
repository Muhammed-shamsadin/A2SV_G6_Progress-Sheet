class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_one = s.count('1')
        count_zero = s.count('0')

        if count_one == 1:
            return ("0"*count_zero) + ("1")
        else:
            return ("1"*(count_one - 1)) + ("0"*count_zero) + ("1")
        
