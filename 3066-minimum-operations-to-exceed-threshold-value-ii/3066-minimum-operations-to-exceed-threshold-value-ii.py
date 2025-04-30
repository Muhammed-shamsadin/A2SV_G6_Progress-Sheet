class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
        
        # print(heap)
        count = 0
        while heap[0] < k:
            x = heappop(heap)
            y = heappop(heap)

            new_val = (min(x, y) * 2 + max(x, y))
            heappush(heap, new_val)

            count += 1
        
        return count

        