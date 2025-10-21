class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        length = len(costs)
        # store the differences of A
        store = []
        for i in range(length):
            diff = costs[i][0] - costs[i][1]
            store.append((diff, i))
        
        # sort the stored differences
        store.sort()

        # calculate the minimum cost
        min_cost = 0
        for i in range(length):
            idx = store[i][1]
            if i < length // 2:
                min_cost += costs[idx][0]
            else:
                min_cost += costs[idx][1]
            
        return min_cost

        # TC -> O(NLogN)
        # SC -> O(2N) -> O(N)
        
        