class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        ans = float('inf') 

        while low <= high:
            mid = (low + high) // 2
            ans = min(nums[mid], ans)

            if nums[low] == nums[high]:
                ans = min(nums[low], ans)
                low += 1
                high -= 1
                continue
            # answer is on the right side of the mid
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1

        return ans