# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        row, col = 0, 0
        direction = 1   # 1 for up & -1 for down
        ans = []

        for i in range(rows * cols):
            ans.append(mat[row][col])

            if direction == 1:
                if col == cols - 1:  # right boundary
                    row += 1
                    direction = -1
                elif row == 0:  # top boundary
                    col += 1
                    direction = -1
                else:
                    row -= 1
                    col += 1
            else:
                if row == rows - 1:  # bottom boundary
                    col += 1
                    direction = 1
                elif col == 0: # left boundary
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1

        return ans
        
                    
