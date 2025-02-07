# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rotate(mat):
            # in another way 90* means, (1. Transpose row, then 2. Reverse the row)
            for i in range(len(mat)):
                for j in range(i):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            mat.reverse()
            

        # There will be 4 possiblities to rotate the matrix right?
        for i in range(4):
            if mat == target:
                return True
            rotate(mat)
            print(mat)
        
        return False