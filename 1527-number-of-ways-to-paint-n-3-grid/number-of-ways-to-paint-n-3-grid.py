class Solution:
    def numOfWays(self, n: int) -> int:
        aba, abc = 6, 6
        for row in range(1,n):
            a_new = 3 * aba + 2 * abc
            b_new = 2 * aba + 2 * abc
            aba, abc = a_new, b_new
        return (aba + abc) % (10**9 + 7)
