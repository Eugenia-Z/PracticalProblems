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
        while right < len(s) and s[right] in set_: # the outer while loop can't control the inner loop's right position effectively, so we need to repeat the condition while right < len(s)
            right += 1
        
        while isValid(s[left:right]):
                res += 1
                left += 1
        # move the left pointer to next character and reset right to left to continue checking
        left = right + 1
        right = left
    return res


## GPT's solution:

def vowelSubstring2(s):
    vowels = set('aeiou')
    left, total_count = 0, 0
    n = len(s)
    
    while left < n:
        if s[left] not in vowels:
            left += 1
            continue
        vowel_count = {v:0 for v in vowels}
        right = left
        
        while right < n and s[right] in vowels:
            vowel_count[s[right]] += 1
            
            if all(vowel_count[v] > 0 for v in vowels):
                total_count += 1
                
            right += 1
        left += 1
    return total_count
if __name__ == "__main__":
    s =  "aaeiouxa"  # output:2
    # s = "axyzaeiou"  # output:1
    print(vowelSubstring2(s))