class Solution:
    def trailingZeroes(self, n: int) -> int:
        '''
        Approach: to get a trailing zeroes the basic logic is to find numbers that are a factors
                of 10. but then since 10 by itself mean 10 = 2 * 5. and while having the value 5
                is more advantageous than having the value 2 for our trailing zeroes, we will try 
                to find numbers which are Factors of 5.
                eg: if we consider 10 the factor, when n = 5, 
                    6 * 5 * 4 * 3 * 2 * 1 = 420, this have only one trailing zeroes, 
                    5! = 5 * 4 * 3 * 2 * 1 = 5! has = 5 * 2 = 10. for larger numbers to get the exact
                trailing zeroes counting numbers which are Factors of 5. will help us get it.
        ''' 

        if n == 0:
            return 0
        
        return (n // 5) + self.trailingZeroes(n // 5)
        