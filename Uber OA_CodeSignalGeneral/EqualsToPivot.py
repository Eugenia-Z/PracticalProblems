# Kaiqi's Solution
def solution1(numbers, pivot):
    res = []
    for num in numbers:
        if num == 0:
            res.append(0)
        elif (num < 0 and pivot < 0) or (num > 0 and pivot > 0):
            res.append(1)
        else:
            res.append(-1)
    return res

if __name__ == "__main__":
    numbers = [6,-5,0]
    pivot = 2
    print(solution1(numbers, pivot))