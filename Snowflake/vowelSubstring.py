## KQ's thought: sliding window approach, with a separate checking function
def isValid(str):
    set_ = set('aeiou')
    set_str = set(str)
    return set_ == set_str

def vowelSubstring(s):
    res = 0
    # sliding window approach
    set_ = set('aeiou')
    left, right = 0, 0
    while right < len(s):
        # move right pointer until we hit a non-vowel
        while right < len(s) and s[right] in set_:
            right += 1
        
        while isValid(s[left:right]):
                res += 1
                left += 1
        # move the left pointer to next character and reset right to left to continue checking
        left = right + 1
        right = left
    return res

if __name__ == "__main__":
    # s =  "aaeiouxa"  # output:1
    s = "axyzaeiou"
    print(vowelSubstring(s))