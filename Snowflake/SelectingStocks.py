## Kaiqi's idea: compute the delta value for each stock, sort in descending order, and return within the initial saving amount
# To keep track of current value, we actually need a tuple to store additional info
# Cannot just go greedy and collect in desc order, has to traverse a bit more candidates to decide -> using heap
import heapq
def selectStock(saving, currentValue, futureValue):
    delta = []
    for curr_value, future_value in zip(currentValue, futureValue):
        delta.append((curr_value - future_value, curr_value, future_value)) # prepare for min_heap
    
    heapq.heapify(delta)
    curr_sum = 0
    while delta:
        
        curr_delta, curr_value, future_value = heapq.heappop(delta)
        if saving - curr_value >=0:
            curr_sum += (-curr_delta)
            saving -= curr_value
    return curr_sum
  
  
## GPT's DP solution:
def selectStock2(saving, currentValue, futureValue):
    n = len(currentValue)
    profit = [futureValue[i] - currentValue[i] for i in range (n)]
    
    # Initialize dp array where dp[i] is the maximum profit with a budget of i
    dp = [0] * (saving + 1)
    
    # Loop over each stock
    for i in range(n):
        cost = currentValue[i]
        gain = profit[i]

        # We only care about stocks with positive profit
        if gain > 0:
            # Update dp array from back to front to prevent overwriting values
            for j in range(saving, cost-1, -1):
                dp[j] = max(dp[j], dp[j-cost] + gain)     
    return max(dp)

if __name__ == "__main__":
    saving = 250
    currentValue = [175, 133, 109, 210, 97]
    futureValue = [200, 125, 128, 228, 133]
    print(selectStock2(saving, currentValue, futureValue))  # output: 55 