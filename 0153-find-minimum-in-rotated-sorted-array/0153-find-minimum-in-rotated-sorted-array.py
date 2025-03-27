class Solution:
    def findMin(self, nums: List[int]) -> int:
        length= len(nums)
        low = 0
        high = length - 1
        ans = float('inf')

        while low <= high:
            mid = (low + high) // 2
            # Left is sorted
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid + 1
            else:
                ans = min(ans, nums[mid])
                high = mid - 1
        return ans