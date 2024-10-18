# KQ's solution
# traverse the readings, and perfom digit-wise summition for every single digit
def solution(readings):
    ans = []
    
    def digitSum(int):
        res = 0
        while int > 0:
            res += int%10
            int //= 10 
        return res

    for reading in readings:
        while reading > 10:
            reading = digitSum(reading)
        ans.append(reading)
    return ans

if __name__ == "__main__":
    readings = [123,456,789,101]
    print(solution(readings))