from collections import Counter
def solution(S):
    # Count frequency of each digit (0 thourhg 9):
    freq = Counter(S)
    
    # Initialize parts of the palindrome
    half_palindrome = []
    middle_digit = None
    
    # Sort the digits in descending order to maximize the value of the palindrome
    for digit in sorted(freq.keys(), reverse=True):
        count = freq[digit]
        
        # Add pairs of digits to the half palindrome
        # In python, multiplying a stirng equals to repition that many # of times
        # if count //2 equals 0, we append an empty string
        # by this step, we're not considering whether count is even or odd yet. we get pairs out it no matter what
        half_palindrome.append(digit * (count // 2))
        
        # Check for a potential middle digit (largest single occurrence)
        if count % 2 == 1:
            if middle_digit is None or digit > middle_digit:
                middle_digit = digit
    
    # Construct the half palindrome string
    half_palindrome_str = ''.join(half_palindrome)
    
    # Form the largest palindrome by mirroring half_palindrome and placing middle_digit in the middle if available.
    if middle_digit:
        largest_palindrome = half_palindrome_str + middle_digit + half_palindrome_str[::-1]
    else:
        largest_palindrome = half_palindrome_str + half_palindrome_str[::-1]

    # Special case:
    if largest_palindrome[0] == '0':
        return middle_digit if middle_digit else '0'
    return largest_palindrome

# Example usage:
# len(S) > 0
# print(solution("00000"))
# print(solution("54315"))
# print(solution("54321"))
