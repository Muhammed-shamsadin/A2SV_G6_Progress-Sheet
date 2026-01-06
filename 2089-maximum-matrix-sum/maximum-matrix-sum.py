class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        rows, cols = len(matrix), len(matrix[0])
        negative_count = 0
        max_negative = float('-inf')
        mini = float('inf')
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] < 0:
                    max_negative = max(max_negative, matrix[row][col])
                    negative_count += 1
                else:
                    mini = min(mini, matrix[row][col])
                total_sum += abs(matrix[row][col])
        # print(total_sum)
        if negative_count % 2 != 0:
            total_sum += 2 * max_negative
            # print(total_sum)
            return max(total_sum, total_sum -2* max_negative - 2* mini)
        
        return total_sum
