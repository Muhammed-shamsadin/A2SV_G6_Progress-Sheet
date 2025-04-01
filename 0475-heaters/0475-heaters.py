class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def check(rad):
            left, right = 0, 0
            while left < len(houses) and right < len(heaters):
                if abs(houses[left] - heaters[right]) <= rad:
                    left += 1
                else:
                    right += 1
            return left == len(houses)
        
        #  BS
        low, high = 0, max(houses[-1], heaters[-1])
        while low <= high:
            mid = low + (high - low) // 2

            if check(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
        