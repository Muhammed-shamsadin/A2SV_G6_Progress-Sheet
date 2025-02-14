# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        scene
        Do not return anything, modify nums in-place instead.
        """
        # not efficient because it creates an extra sapce & it is out-of-place
        # k = k % len(nums)
        # # here nums[-k:] + nums[:-k], creates a new list of size o(n)
        # nums[:] = nums[-k:] + nums[:-k]

        # efficient TC -> O(N),  SC -> O(1)
        k = k % len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

