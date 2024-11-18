import heapq

def getTotalImpact(initialReelImpacts, newReelImpacts, k) -> int:

    # min_heap of size k, so that min_heap[0] is always the kth largest element 
    min_heap = [-1] * k
    for element in initialReelImpacts:
        heapq.heappushpop(min_heap, element)

    # by now the top of the heap is init impact
    impact  = min_heap[0]

    # process the new impact
    for element in newReelImpacts:
        heapq.heappushpop(min_heap, element)
        impact += min_heap[0]
    return impact

# example code:
# initialReelImpacts = [2, 3]
# newReelImpacts = [4, 5, 1]
# k = 2
initialReelImpacts = [2, 2, 4]
newReelImpacts = [3, 3, 5]
k = 2
impact = getTotalImpact(initialReelImpacts, newReelImpacts, k)
print("Total impact is: ", impact)