def maxSubArray(nums):
    minCount = float('inf')
    frequencyMap = defaultdict(int)
    
    for num in nums:
        frequencyMap[num] += 1
    
    for freq in frequencyMap.values():
        minCount = min(minCount, freq)
    
    maxLength = 0
    left = 0
    countMap = defaultdict(int)
    
    for right in range(len(nums)):
        countMap[nums[right]] += 1
        
        while countMap[nums[right]] > minCount:
            countMap[nums[left]] -= 1
            left += 1
        
        maxLength = max(maxLength, right - left + 1)
    
    return maxLength
