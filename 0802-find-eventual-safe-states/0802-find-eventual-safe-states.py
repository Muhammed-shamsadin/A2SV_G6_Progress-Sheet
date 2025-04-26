class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outdegree = [0 for _ in range(len(graph))]
        for i in range(len(graph)):
            outdegree[i] = len(graph[i])

        
        visited = set()
        terminal = set()
        for i in range(len(outdegree)):
            if outdegree[i] == 0:
                terminal.add(i)
        def dfs(node):
            if node in terminal:
                return True

            if node in visited:
                return False
            
            visited.add(node)
            for neighbours in graph[node]:
                if not dfs(neighbours):
                    return False

            terminal.add(node)
            return True
        
        for i in range(len(graph)):
            if i not in visited:
                dfs(i)
        
        res = list(terminal)
        res.sort()
        return res




