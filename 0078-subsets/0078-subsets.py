class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        for i in range(2 ** len(nums)):
            temp = []
            for j in range(len(nums)):
                if i & (1 << j) != 0:
                    temp.append(nums[j])
            subsets.append(temp)
        
        return subsets
