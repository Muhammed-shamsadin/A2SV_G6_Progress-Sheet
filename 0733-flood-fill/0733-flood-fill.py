class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        graph = defaultdict(list)
        queue = deque([(sr, sc)])


        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        visited.add((sr, sc))
        prev = image[sr][sc]
        image[sr][sc] = color

        def inbound(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])
        
        while queue:
            row, col = queue.popleft()

            for x, y in directions:
                nr = row + x
                nc = col + y

                if inbound(nr, nc) and (nr, nc) not in visited and image[nr][nc] == prev:
                    image[nr][nc] = color
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        
        return image
