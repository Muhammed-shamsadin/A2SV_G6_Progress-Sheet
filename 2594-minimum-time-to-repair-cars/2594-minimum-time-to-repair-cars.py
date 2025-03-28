class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def check(mid):
            count = 0
            for num in ranks:
                count += math.floor(math.sqrt(mid // num))

            return count >= cars

        low, high = 0, min(ranks)*(cars**2)
        res = float('inf')
        while low <= high:
            mid = (low + high) // 2

            if check(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res