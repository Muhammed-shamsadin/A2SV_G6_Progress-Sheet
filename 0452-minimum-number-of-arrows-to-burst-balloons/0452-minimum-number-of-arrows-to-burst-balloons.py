class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        arrow = 1
        last = points[0][1]
        for start, end in points:
            if start <= last:
                last = min(last,end)
                continue
            last = end
            arrow += 1

        return arrow