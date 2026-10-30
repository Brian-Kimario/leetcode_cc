class Solution(object):
    def numIslands(self, grid):
        
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            # Base case: if out of bounds or sitting on water, stop
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
                
            # Mark the current cell as visited by sinking it to '0'
            grid[r][c] = '0'
            
            # Explore all 4 adjacent directions (up, down, left, right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        # Traverse every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    # Found a new island, trigger DFS to sink the entire island
                    island_count += 1
                    dfs(r, c)
                    
        return island_count
