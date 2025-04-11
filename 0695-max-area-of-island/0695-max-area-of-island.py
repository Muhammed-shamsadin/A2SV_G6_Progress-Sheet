class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0, -1), (-1,0)]
        visited = set()
        max_Area = 0
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            visited.add((row, col))

            count = 0
            for x, y in directions:
                new_row = row + x
                new_col = col + y
            
                if inbound(new_row, new_col) and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                    count += 1
                    count += dfs(new_row, new_col)

            return count
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited:
                    max_Area =  max(max_Area, dfs(row, col))

        return max_Area
        
        
        

            

            



        

