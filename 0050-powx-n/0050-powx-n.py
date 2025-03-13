class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
        
        n = abs(n)
        
        def power(num):
            if num == 0:
                return 1
            half = power(num // 2)
            half **= 2

            if num % 2 != 0:
                half *= x
            
            return half
        
        return power(n)