class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0

        for i in range(1, len(points)):
            a, b = points[i]
            x = abs(a - points[i - 1][0])
            y = abs(b - points[i - 1][1])
            res += max(x, y)

        return res

