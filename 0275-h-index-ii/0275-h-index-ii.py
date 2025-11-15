class Solution:
    def hIndex(self, citations: List[int]) -> int:


        def valid(h):
            idx = bisect_left(citations, h)
            count = len(citations) - idx

            return count >= h

        left = 0
        right = max(citations)
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if valid(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
