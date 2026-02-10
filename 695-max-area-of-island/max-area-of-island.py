class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS
        max_Area = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(r, c):
            visited.add((r,c))

            count = 1
            for x, y in directions:
                new_r, new_c = r + x, c + y

                if inbound(new_r, new_c) and grid[new_r][new_c] == 1 and (new_r, new_c) not in visited:
                    count += dfs(new_r, new_c)
            
            return count
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 1:
                    max_Area = max(max_Area, dfs(i,j))
        

        return max_Area