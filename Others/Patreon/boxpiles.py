
# sort the boxexInPile in descending order. 
# the key insight is that as we traverse, the number of steps needed to reduce all the previous piles to current pile is equal to the number of piles before this one -> which is easy to get just by the index number
# Each time we encounter a shorter height in the sorted list, we increment the steps by the number of piles we've passed so far. Since these are the taller piles that need to be reduced.
def sol(nums):
    count = 0
    nums.sort(reverse = True)
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            count += i
    return count

if __name__ == "__main__":
    nums = [4, 5, 5, 4, 2]
    res = sol(nums)
    print(res)