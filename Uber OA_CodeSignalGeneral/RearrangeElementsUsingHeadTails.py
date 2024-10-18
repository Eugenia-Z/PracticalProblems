# KQ's intuition: use recursion
def solution1(numbers):
    res = []
    def recursion(numbers):
        if not numbers:
            return
        if len(numbers) == 1:
            # this is the middle element in an odd-length array
            res.append(numbers[0])
        else:
            res.append(numbers[0])
            res.append(numbers[-1])
        return recursion(numbers[1:len(numbers)-1])
    
    recursion(numbers)
    return res

# GPT's approach: two pointers iterative approach
def solution2(numbers):
    left, right = 0, len(numbers)-1
    res = []
    while left <= right:
        if left == right:
            # this is the middle element in an odd-lenght array
            res.append(numbers[left])
        else:
            res.append(numbers[left])
            res.append(numbers[right])
        left += 1
        right -= 1
    return res

if __name__ == "__main__":
    numbers = [1,3,5,6,7]
    print(solution2(numbers))
    