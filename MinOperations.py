def can_complete_in_operations(arr, x, y, max_operations):
    operations = 0
    for num in arr:
        if num <= max_operations + y:
            continue
        else:
            remaining = num - max_operations * y
            if remaining > 0:
                operations += (remaining + x - y - 1) // (x - y)
            if operations > max_operations:
                return False
    return True

def min_operations(arr, x, y):
    left, right = 0, max(arr) // y + 1
    result = right
    while left <= right:
        mid = left + (right - left) // 2
        if can_complete_in_operations(arr, x, y, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result