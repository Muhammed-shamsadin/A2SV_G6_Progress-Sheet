# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        '''
        Approach: Everytime the bottle get's exchanged with a limited number of bottles, so 
         we keep performing the same iterations, Step 1: we divide the number of bottles to be refilled
         with the numExchange, and then Step 2: the modulos of those numbers will give us a remainder
         which is the bottle that cannot be filled now but it can be added with the bottles that is
         being dranked and then we will sum these bottles and exchange them. doing this iteratively until
         the numBottle is lessthan numExchange.
        '''
        res = numBottles
        while numBottles >= numExchange:
            quotient = numBottles // numExchange 
            remainder = numBottles % numExchange 

            res += quotient
            numBottles = quotient + remainder
        
        return res
            
