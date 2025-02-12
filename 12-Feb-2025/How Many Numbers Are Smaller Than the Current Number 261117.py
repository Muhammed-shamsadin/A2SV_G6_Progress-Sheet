# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        k = sorted(nums)
        res = []
        count = Counter()

        for index, key in enumerate(k):
            if key not in count:
                count[key] = index
        
        for num in nums:
            res.append(count[num])
        
        return res