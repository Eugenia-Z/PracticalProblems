from collections import deque
def BFSSolution(plan):
    rows, cols = len(plan), len(plan[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    def bfs(r, c):
        # Queue-based BFS to mark all connected dirty cells as visited
        queue = deque([(r, c)])
        while queue:
            x, y = queue.popleft()
            # Check boundaries
            if x < 0 or x >= rows or y < 0 or y >= cols:
                continue            
            # Skip if already visited or if it's a wall
            if visited[x][y] == True or plan[x][y] == '#':
                continue
            
            # Visit the current cell and enqueue all the four possible directions
            visited[x][y] = True
            queue.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])
            
    runs = 0
    for i in range(rows):
        for j in range(cols):
            # Start BFS for each unvisited dirty cell
            if plan[i][j] == '*' and not visited[i][j]:
                bfs(i, j)
                runs += 1
    return runs
                

# Example usage
plan = ['.*#..*', '.*#*.#', '######', '.*..#.', '...###']
print(BFSSolution(plan))