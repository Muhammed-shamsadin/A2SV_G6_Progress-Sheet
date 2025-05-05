class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        def check(mid):
            diff = [] 
            for i in range(mid):
                h = heights[i + 1] - heights[i]
                if h > 0:
                    diff.append(h)
            
            diff.sort(reverse=True)
            
            use_bricks = diff[ladders:]
            total_needed_bricks = sum(use_bricks)

            return total_needed_bricks <= bricks

        
        low, high = 0, len(heights) - 1
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans