# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        area = 0
        maximum_water = 0


        while left < right:
            minimum = min(height[left], height[right])

            area = (right - left) * minimum
            maximum_water = max(area, maximum_water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maximum_water