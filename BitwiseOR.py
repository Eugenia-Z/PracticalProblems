def findAllBitOrSeq(nums):
    n = len(nums)
    result = []
    maxValue = 0

    for num in nums:
        maxValue |= num

    dp = [0] * (maxValue + 1)
    dp[0] = 1

    for num in nums:
        for i in range(maxValue + 1):
            if dp[i] > 0 and num > i:
                dp[i | num] += dp[i]
            else:
                dp[num] = 1

    for i in range(maxValue + 1):
        if dp[i] > 0:
            result.append(i)

    return result
