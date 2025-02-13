# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        length = len(costs)
        maxim = max(costs)
        count = [0] * (maxim + 1)

        for i in costs:
            count[i] += 1

        check = 0
        max_bars = 0

        for i in range(maxim + 1):
            while count[i] > 0 and check +  i <= coins:
                check += i
                count[i] -= 1
                max_bars += 1
            

        return max_bars