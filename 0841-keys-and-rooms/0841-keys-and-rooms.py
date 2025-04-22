class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for i in range(len(rooms)):
            for items in rooms[i]:
                graph[i].append(items)
        
        # print(graph)
        visited = set([0])
        queue = deque([0])
        cnt = 0

        while queue:
            node = queue.popleft()
            # print(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
            
            cnt += 1

        # print(cnt)

        if cnt >= len(rooms):
            return True
        else:
            return False

