def match_sub_array_result(capacity):
    val_to_index = {}
    n = len(capacity)
    pre_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        pre_sum[i] = pre_sum[i - 1] + capacity[i - 1]

    ans = 0
    for i in range(2, n):
        val_to_index[capacity[i - 2]] = i - 1
        if capacity[i] in val_to_index:
            if pre_sum[i] - pre_sum[val_to_index[capacity[i]]] == capacity[i]:
                ans += 1

    return ans