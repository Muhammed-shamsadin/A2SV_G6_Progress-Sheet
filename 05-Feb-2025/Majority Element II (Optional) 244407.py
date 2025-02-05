# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        prob = len(nums) // 3
        count = Counter(nums)

        ans = []
        for key, value in count.items():
            if value > prob:
                ans.append(key)
        
        return ans

