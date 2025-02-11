# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        left, right = 0, cols - 1
        top, bottom = 0, rows - 1

        ans = []

        while left <= right and top <= bottom:

            # left -> right
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # top -> bottom
            for j in range(top, bottom + 1):
                ans.append(matrix[j][right])
            right -= 1

            if top <= bottom:
                # right -> left
                for k in range(right, left - 1, -1):
                    ans.append(matrix[bottom][k])
                bottom -= 1

            if left <= right: 
                # bottom -> top
                for l in range(bottom, top - 1, -1):
                    ans.append(matrix[l][left])
                left += 1

        return ans