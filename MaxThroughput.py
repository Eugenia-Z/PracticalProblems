def canAchieve(throughput, scaling_cost, budget, target):
    totalCost = 0
    for i in range(len(throughput)):
        if throughput[i] >= target:
            continue
        requiredIncrease = (target - 1) // throughput[i]
        cost = requiredIncrease * scaling_cost[i]
        totalCost += cost
        if totalCost > budget:
            return False
    return totalCost <= budget

def getMaximumThroughput(throughput, scaling_cost, budget):
    left = 1
    right = max(throughput)
    
    for i in range(1, len(throughput)):
        right = max(right, throughput[i] + (budget // scaling_cost[i]) * throughput[i])
    
    result = left
    
    while left <= right:
        mid = left + (right - left) // 2
        if canAchieve(throughput, scaling_cost, budget, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result