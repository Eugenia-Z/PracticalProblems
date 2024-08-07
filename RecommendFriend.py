def find_index_recommend(root, arr, vec):
    index = float('inf')  # Initialize index to the largest integer value
    mp = {}  # Use a dictionary to record elements in the array

    # Mark elements in the array
    for i in arr:
        mp[i] = 1

    # Iterate through the array
    for x in arr:
        for j in vec[x]:
            # Skip if already in the array
            if j in mp:
                continue
            # Update index if a better recommendation is found
            if j != root and index > j:
                index = j

    # Return -1 if no recommendation is found, otherwise return the index
    return -1 if index == float('inf') else index


def find_recommend_friend(n, m, friendships):
    vec = [[] for _ in range(n + 1)]

    # Clear adjacency list for each node
    for i in range(n + 1):
        vec[i].clear()

    # Build the graph based on friendships
    for x, y in friendships:
        vec[x].append(y)
        vec[y].append(x)

    ans = []  # Store recommended friends for each user

    # Iterate through each user
    for i in range(n):
        first_layer = vec[i]  # Get the first layer of friends for the user
        ans.append(find_index_recommend(i, first_layer, vec))  # Find and store recommended friends

    return ans