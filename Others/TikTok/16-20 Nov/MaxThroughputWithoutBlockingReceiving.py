def max_throughput(serverTasks):
    n = len(serverTasks)
    
    def helper(index):
        if index >= n:  # Base case: no more servers
            return 0
        
        # Skip server `index`
        skip = helper(index + 1)
        
        # Use server `index` for handoff
        next_server = serverTasks[index]
        use = index + helper(index + 1)  # Include current server's index
        
        # Return the maximum score
        return max(skip, use)
    
    return helper(0)

# Example usage
serverTasks = [3, 0, 1, 2]  # Replace with the input array
print("Maximum Throughput Score:", max_throughput(serverTasks))
