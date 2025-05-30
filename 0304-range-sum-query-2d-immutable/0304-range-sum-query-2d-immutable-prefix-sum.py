class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.pref = [[0] * (cols + 1) for i in range(rows + 1)] 

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                self.pref[row][col] = self.pref[row][col - 1] + self.pref[row - 1][col] - self.pref[row - 1][col - 1] + matrix[row - 1][col - 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        result = self.pref[row2][col2] - self.pref[row2][col1 - 1] - self.pref[row1 - 1][col2] + self.pref[row1 - 1][col1 - 1]

        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)