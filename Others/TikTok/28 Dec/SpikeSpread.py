# input: array of activity Index, 

from collections import defaultdict


def getTopKViralPosts(activityIndex, k):
    
    binary_strs = []
    index_to_gap = defaultdict(int)
    
    # convert each activityIndex to binary
    for index in activityIndex:
        # convert to binary
        bin_str = bin(index)[2:]
        
        max_gap = -1
        last_index = -1
        # compute max gap between spikes (1s)
        for idx, char in enumerate(bin_str):
            if char == "1":
                if last_index != -1:
                    max_gap = max(max_gap, idx-last_index)
                last_index = idx
        
        # stored together with activtityScore itself
        index_to_gap[index] = max_gap
        
    # return top k (if gap has a tie, take the activtityScore with a higher value)
    gap_to_index_sorted = dict(sorted(index_to_gap.items(), key=lambda x:(-x[1], -x[0])))
    return list(gap_to_index_sorted.keys())[:k]

activityIndex = [3,5,8]
k = 1
print(getTopKViralPosts(activityIndex, 1))