class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}

        def dp(i, j):
            if i == len(s1):
                memo[(i, j)] = sum(ord(c) for c in s2[j:])
                return memo[(i, j)]
            
            if j == len(s2):
                memo[(i, j)] = sum(ord(c) for c in s1[i:])
                return memo[(i, j)]

            if (i, j) in memo:
                return memo[(i, j)]

            if s1[i] == s2[j]:
                memo[(i, j)] = dp(i+1, j+1)
                return memo[(i, j)]
            else:
                memo[(i, j)] = min(ord(s1[i]) + dp(i+1, j), ord(s2[j]) + dp(i, j+1))
                return memo[(i, j)]

            
        return dp(0, 0)