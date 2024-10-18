# KQ's solution
# traverse the readings, and perfom digit-wise summition for every single digit
def solution(readings):
    freq = {}
    
    def digitSum(num):
        res = 0
        while num > 0:
            res += num%10
            num //= 10 
        return res

    for reading in readings:
        # Reduce the number to a single digit 
        while reading >= 10:
            reading = digitSum(reading)
        freq[reading] = freq.get(reading,0)+1
    
    # Sort the frequency dict by frequency first then by key 
    freq_sorted = dict(sorted(freq.items(),key = lambda item:(item[1],item[0]), reverse = True))
    
    # Access the first key from the sorted dictionary 
    return list(freq_sorted.keys())[0]

# GPT's solution

if __name__ == "__main__":
    readings = [123,456,789,101]
    print(solution(readings))

