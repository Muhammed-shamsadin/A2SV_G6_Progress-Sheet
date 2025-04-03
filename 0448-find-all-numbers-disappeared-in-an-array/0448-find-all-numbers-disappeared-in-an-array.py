class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        ans = []

        while i < n:
            corr = nums[i] - 1
            if nums[corr] != nums[i]:
                nums[corr], nums[i] = nums[i], nums[corr]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                ans.append(i + 1)
        
        return ans
