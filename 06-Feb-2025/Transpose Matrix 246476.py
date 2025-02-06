# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        ans = []

        for col in range(cols):
            res = []
            for row in range(rows):
                res.append(matrix[row][col])
            ans.append(res)
        
        return ans
