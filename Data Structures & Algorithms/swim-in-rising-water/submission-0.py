class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        size = len(grid)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set([(0, 0)])
        queue = [(grid[0][0], 0, 0)]
        
        def is_in_grid(idx: int, idy: int) -> bool:
            return idx >= 0 and idx < size and idy >= 0 and idy < size

        while queue:
            t, idx, idy = heapq.heappop(queue)
            if idx == size - 1 and idy == size - 1:
                return t
            for direction in directions:
                x = idx + direction[0]
                y = idy + direction[1]
                if is_in_grid(x, y) and (x, y) not in visited:
                    visited.add((x, y))
                    heapq.heappush(queue, (max(t, grid[x][y]), x, y))
        
        return 0