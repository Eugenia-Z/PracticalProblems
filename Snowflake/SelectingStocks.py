## Kaiqi's idea: compute the delta value for each stock, sort in descending order, and return within the initial saving amount
# To keep track of current value, we actually need a tuple to store additional info
# Cannot just go greedy and collect in desc order, has to traverse a bit more to decide 
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
   

if __name__ == "__main__":
    saving = 250
    currentValue = [175, 133, 109, 210, 97]
    futureValue = [200, 125, 128, 228, 133]
    print(selectStock(saving, currentValue, futureValue))