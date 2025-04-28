class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])

        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def notInBorder(row, col):
            return 1 <= row < (rows - 1) and 1 <= col < (cols - 1)
        
        def dfs(row, col):
            for x, y in directions:
                new_row, new_col = row + x, col + y

                if notInBorder(new_row, new_col) and inbound(new_row, new_col) and board[new_row][new_col] == "O":
                    board[new_row][new_col] = "X"
                    dfs(new_row, new_col)


        def dfs2(row, col):
            nonlocal is_Ocean
            visited.add((row, col))
            
            if not notInBorder(row, col):
                is_Ocean = True
            

            for x, y in directions:
                new_row, new_col = row + x, col + y

                if inbound(new_row, new_col) and (new_row, new_col) not in visited and board[new_row][new_col] == "O":
                    dfs2(new_row, new_col)


        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O' and (row, col) not in visited:
                    is_Ocean = False
                    dfs2(row, col)

                    if not is_Ocean:
                        board[row][col] = "X"
                        dfs(row, col)

                

