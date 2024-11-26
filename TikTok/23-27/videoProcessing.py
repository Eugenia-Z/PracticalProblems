# similar to house robber problems where adjacent values interfere with each other
# pre-processing: count the frequency -> this is our multiplier when populating the DP value
from collections import Counter
def maxProcessingPower(processingPower):
    freq = Counter(processingPower)
    unique_powers = sorted(freq.keys())
    
    # edge case:
    if len(unique_powers) == 1:
        return unique_powers[0] * freq[unique_powers[0]]
    
    # init DP -> Note the DP size here 
    dp = [0] * len(unique_powers)
    dp[0] = unique_powers[0] * freq[unique_powers[0]]
    
    # populate DP array: 
    for i in range(1, len(unique_powers)):
        curr_power = unique_powers[i] * freq[unique_powers[i]]
        
        # if the previous power interferes (because we've sorted it before, all we need to do is compare "+1" situation, not "-1")
        if unique_powers[i] == unique_powers[i-1] + 1:
            dp[i] = max(dp[i-1], dp[i-2] + curr_power if i>1 else curr_power)
        else:
            dp[i] = dp[i-1] + curr_power
    return dp[-1]

# Example input:
# processingPower = [1, 3, 9, 2, 3]
# processingPower = [3, 3, 5, 5, 2, 2, 5]
processingPower = [8, 5, 1, 5]
print(maxProcessingPower(processingPower))