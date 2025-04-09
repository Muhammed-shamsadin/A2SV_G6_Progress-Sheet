class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(set)

        for a, b in trust:
            graph[a].add(b)
        
        
        for i in range(1, n + 1):
            if not graph[i]:
                flag = True
                for j in range(1,n+1):
                    if i == j:
                        continue
                    if graph[j] and i not in graph[j]:
                        flag = False
                        break
                if flag:
                    return i
        
        return -1

