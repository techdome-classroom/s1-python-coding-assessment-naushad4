class Solution:
    def getTotalIsles(self, grid):
        if not grid:
            return 0
        
        
        rows = len(grid)
        cols = len(grid[0])

    
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        
        def dfs(r, c):
            visited[r][c] = True
            
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                if 0 <= new_r < rows and 0 <= new_c < cols and not visited[new_r][new_c] and grid[new_r][new_c] == 'L':
                    dfs(new_r, new_c)
        
        
        num_islands = 0
        
        
        for r in range(rows):
            for c in range(cols):
            
                if grid[r][c] == 'L' and not visited[r][c]:
                    num_islands += 1
                    dfs(r, c)
        
        return num_islands
