def IterativeDFSsolution(plan):
    rows, cols = len(plan), len(plan[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    def dfs(row, col):
        # Stack-based DFS to mark all connected dirty cells as visited
        stack = [(row, col)]
        while stack:
            x, y = stack.pop()
            
            # Handle boundaries
            if x < 0 or x >= rows or y < 0 or y >= cols:
                continue
            # Skip if already visited or if it's a wall
            if visited[x][y] or plan[x][y] == '#':
                continue
            
            # Mark this cell as visited and add all four possible directions
            visited[x][y] = True
            stack.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])
        
    runs = 0
    for i in range(rows):
        for j in range(cols):
            # Start DFS for each unvisited dirty cell
            if plan[i][j] == '*' and not visited[i][j]:
                dfs(i, j)
                runs += 1  # Each DFS means one cleaning run
    return runs


# Example usage
plan = ['.*#..*', '.*#*.#', '######', '.*..#.', '...###']
print(IterativeDFSsolution(plan))
