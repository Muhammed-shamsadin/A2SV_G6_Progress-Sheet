class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        if k > sum(candies): return 0

        def check(mid):
            count = 0
            for num in candies:
                count += (num // mid)
            
            return count >= k 

        result = float('-inf')
        low, high = 1, max(candies)
        while low <= high:
            mid = (low + high) // 2
            
            # count > k: move-low , else:  # count < k
            if check(mid):
                result = max(mid, result)
                low = mid + 1
            else:
                high = mid - 1

        return result