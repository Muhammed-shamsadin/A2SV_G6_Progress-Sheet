class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        memo = {}

        # max dot product of two subsequences starting at i,j
        def dp(i,j):

            if i == len(nums1) or j == len(nums2):
                return float("-inf") # if we are passed the boundary, dont pick anything from there.

            if (i,j) in memo:
                return memo[(i,j)]

            take = nums1[i] * nums2[j]

            # take i,j. move forward, or  # take this subsequence and just end., or # skip i: i+1,j, or # skip j: i,j+1
            res = max(take + dp(i+1, j+1), take, dp(i+1,j), dp(i,j+1))

            memo[(i,j)] = res

            return memo[(i,j)]

        return dp(0,0)