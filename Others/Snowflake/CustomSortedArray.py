# Kaiqi's idea: 1/ helper function to compute odd or even 
# 2/ two pointer, one traverse from right to left counting even, one from left to right counting odd. 
# Swap whenever needed and count the # of swaps
def isEven(n):
    return n % 2 == 0

def moves(arr):
    left, right = 0, len(arr)-1
    count = 0
    while left < right:
        while left < len(arr) and isEven(arr[left]):
            left += 1
        while right >= 0 and not isEven(arr[right]):
            right -= 1
        if left < right:
            # we found an odd number on the left and an even number on the right that need to be swapped
            arr[left], arr[right] = arr[right], arr[left]
            count += 1
            left += 1
            right -= 1
    return count
if __name__ == "__main__":
    arr = [6, 3, 4, 5]
    print(moves(arr))