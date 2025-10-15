class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        
        result = 0
        x = abs(x)
        while x > 0:
            curr_digit = x % 10
            x //= 10
            result = result * 10 + curr_digit
        
        result = result if not is_negative else -1 * result
        
        return result 
        """
        is_negative = x < 0
        
        result = 0
        
        while x > 0:
            curr_digit = x % 10
            x //= 10
            result = result * 10 + curr_digit
        
        result = result if not is_negative else - result
        
        return result 
        
        """