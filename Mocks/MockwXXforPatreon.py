""" Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. 
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9 """

""" def sol(nums):
    if len(nums) == 0:
        return 0 

    # sort the input array
    nums.sort()
    
    # traverse through the elements
    ans = 0
    i = 0
    j = 1
    n = len(nums)
    while j < n and i < n:
        while nums[j] == nums[j-1] + 1:
            j += 1
        ans = max(ans, j - i)
        i = j 
        j += 1
    return ans

# example run
nums = [100,4,200,1,3,2]
sorted = [1,2,2,3,4,100,200]
i = 0 -> 4
j = 1 -> 2 -> 3 -> 4
ans = 4 """

def sol(nums):
    set_ = set(nums)
    ans = 0
    
    for num in set_:
        count = 1
        if num-1 not in set_:
            # num is the starting point of a sequence
            next = num + 1
            while next in set_:
                count += 1
                next += 1
            ans = max(ans, count)
        else:
            continue
    return ans
            

# example: 
# nums = [1,2,2,3,4,100,200]
# nums = [0,3,7,2,5,8,4,6,0,1]
nums = [1]
print(sol(nums))
# num: 2
# count = 4
# next: 5
# ans: 4

# ans = 4