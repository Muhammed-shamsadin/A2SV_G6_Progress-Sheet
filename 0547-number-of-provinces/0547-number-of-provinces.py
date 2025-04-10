class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0

        # convert into adjacency list
        graph = defaultdict(list)

        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):

                if isConnected[row][col] == 1 and row != col:
                    graph[row].append(col)
                    graph[col].append(row)
        
        # dfs into every node
        def dfs(node):
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        
        for node in range(len(isConnected)):
            if node not in visited:
                count += 1
                dfs(node)
        
        return count
            
        



                
