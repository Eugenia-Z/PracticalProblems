# Kaiqi's Thought: Greedy strategy: each time take the chocalate with the max weigths, compute half and put it back to.
# Use a heap for fast access of the max value (python uses min heap, so flip the sign: using -1)
import heapq
import math

def findMinWeight(weights, d):
    new_weights = [weight * (-1) for weight in weights]
    heapq.heapify(new_weights)
    
    while d > 0:
        curr = heapq.heappop(new_weights)
        curr *= -1
        after_eat = (curr - math.floor(curr/2))
        after_eat *= -1
        heapq.heappush(new_weights, after_eat)
        d -= 1
        
    return sum([weight *(-1) for weight in new_weights])

# GPT's approach is the same, just neater syntax
def findMinWeight2(weights, d):
    max_heap = [-w for w in weights]
    heapq.heapify(max_heap)
    
    for _ in range(d):
        heaviest = -heapq.heappop(max_heap)
        remaining = heaviest // 2  # floor division by 2
        heapq.heappush(max_heap, -remaining)
    return -sum(max_heap)
        
if __name__ == "__main__":
    weights = [30, 20, 25]
    d = 4
    print(findMinWeight(weights, d))
    
    