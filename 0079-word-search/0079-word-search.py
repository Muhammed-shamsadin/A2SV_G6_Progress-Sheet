class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols
             

        def search(row, col, index):
            if index == len(word):
                return True
            
            if board[row][col] != word[index]:
                return False
            
            visited.add((row, col))

            for x, y in directions:
                next_row, next_col = row + x, col + y
                
                if inbound(next_row, next_col) and (next_row, next_col) not in visited:
                    if search(next_row, next_col, index + 1):
                        return True
            
            visited.remove((row, col))
        
            return False
        
        for row in range(rows):
            for col in range(cols):
                if search(row, col, 0):
                    return True
        
        return False
             

