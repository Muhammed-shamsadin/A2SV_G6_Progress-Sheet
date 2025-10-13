class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(grid), len(grid[0])

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def dfs(row, col):
            visited.add((row, col))
            
            for x, y in directions:
                new_row, new_col = row + x, col + y

                if inbound(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == '1':
                    dfs(new_row, new_col)
            
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    islands += 1
                    dfs(row, col)

        return islands

        
                    
        
        
