class RecentCounter:

    def __init__(self):
        self.request = []

    def ping(self, t: int) -> int:
        start, end = t - 3000, t
        self.request.append(t)
        count = 0

        for i in range(len(self.request)):
            if self.request[i] >= start and self.request[i] <= end:
                count += 1
        
        return count
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# return [t-3000, t]
# 