# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        length = len(piles)
        maximum_coins = 0
        k = length // 3

        piles.sort()

        for i in range((length - 2), -1, -2):
            if k > 0:
                maximum_coins += piles[i]
            k -= 1

        return maximum_coins