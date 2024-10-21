"""GPT's solution, with 2 test cases seems to work fine"""
def getMinCost(cost, time):
    n = len(cost)
    MOD = 10**9 + 7
    
    # DP array to store the minimum cost to process tasks up to task i
    dp = [float('inf')] * n
    dp[0] = cost[0]  # The first task must be run on paid server
    
    # Track the last task that can allow running a free server job
    last_paid_server_task = 0
    
    # Iterate through each task
    for i in range(1, n):
        dp[i] = dp[i-1] + cost[i]  # run the current task i on the paid server
        
        while last_paid_server_task < i and time[last_paid_server_task] <= 1:
            last_paid_server_task += 1
        if last_paid_server_task < i:
            dp[i] = min(dp[i], dp[last_paid_server_task])
    return dp[n-1] % MOD

if __name__ == "__main__":
    cost = [1, 1, 3, 4]
    time = [3, 1, 2, 3]  # output: 1
    # cost = [1, 1, 3, 4]
    # time = [3, 1, 2, 3]  # output: 3
    print(getMinCost(cost, time))