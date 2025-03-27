class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(mid, days):
            curr_sum = 0
            count_days = 1

            for right in range(len(weights)):
                if curr_sum + weights[right] > mid:
                    if weights[right] <= mid:
                        curr_sum = weights[right]
                        count_days += 1
                    else:
                        return False
                else:
                    curr_sum += weights[right]
                    
            
            return count_days <= days

        
        total_weight = sum(weights)
        low, high = 1, total_weight

        while low <= high:
            mid = (low + high) // 2

            if check(mid, days):
                print(check(mid, days))
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans