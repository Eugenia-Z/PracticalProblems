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
# Note that: to deal with sorting in case of a tie, just pass a tuple to lambda function -> key=lambda x:(frequency[x], x)

from collections import Counter
def digit_root(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num
def solution2(readings):
    # Step 1: transform each number to its digit root (single digit form)
    transformed = [digit_root(num) for num in readings]  # calling the helper function on the go
    
    # Step2: counting the occurrences of each digit
    frequency = Counter(transformed)
    #print(frequency)

    # Step3: Find the most frequent digit. In case of a tie, return the highest digit
    most_frequent_digit = max(frequency, key=lambda x:(frequency[x], x))   
    return most_frequent_digit

if __name__ == "__main__":
    readings = [123,456,789,101]
    print(solution2(readings))

