def max_throughput(serverTasks):
    n = len(serverTasks)
    used = set()  # Set to track locked servers (already used)
    
    def helper(index):
        if index >= n:  # Base case: no more servers
            return 0
        if index in used:  # Skip locked servers
            return helper(index + 1)
        
        # Skip server `index`
        skip = helper(index + 1)
        
        # Use server `index` if possible
        use = 0
        next_server = serverTasks[index]
        if next_server < n and next_server != index and next_server not in used:
            # Temporarily lock servers
            used.add(index)
            used.add(next_server)
            use = index + next_server + helper(index + 1)
            # Unlock after backtracking
            used.remove(index)
            used.remove(next_server)
        
        # Return the maximum score
        return max(skip, use)
    
    return helper(0)

# Example usage
serverTasks = [3, 0, 1, 2]  # Replace with the input array
print("Maximum Throughput Score:", max_throughput(serverTasks))
