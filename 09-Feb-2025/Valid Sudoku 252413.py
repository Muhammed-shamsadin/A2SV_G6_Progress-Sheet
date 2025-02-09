# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count_rows = defaultdict(set)
        count_cols = defaultdict(set)
        count_grid = defaultdict(set)
        
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val in count_rows[row] or val in count_cols[col] or val in count_grid[(row // 3, col // 3)]:
                    return False

                if val.isdigit():
                    count_rows[row].add(val)
                    count_cols[col].add(val)
                    count_grid[(row // 3, col // 3)].add(val)
                
        return True
        