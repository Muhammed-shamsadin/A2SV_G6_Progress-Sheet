# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counter = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i]*nums[j]
                counter[product] += 1
        
        count = 0
        for val in counter.values():
            if val >= 2:
                count += (val * (val - 1)) // 2
        
        return 8 * count
