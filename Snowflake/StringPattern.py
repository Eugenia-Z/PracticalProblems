# GPT Solution:
MOD = 10**9 + 7
def calculateWays(wordLen, maxVowels):
    # DP table: dp[i][j] means length `i` word ends with `j` consecutive vowels
    dp = [[0] * (maxVowels + 1) for _ in range(wordLen + 1)]
    
    # Base case: there's 1 way to have an empty word
    dp[0][0] = 1
    
    # Precompute number of vowels and consonants
    vowels = 5
    consonants = 21
    
    # Fill the DP table
    for i in range(1, wordLen + 1):
        # Case 1: Add a consonant, which resets the count of consecutive vowels
        dp[i][0] = sum(dp[i-1]) * consonants % MOD
        
        # Case 2: Add a vowel, which increases the count of consecutive vowels.
        for j in range(1, maxVowels + 1):
            dp[i][j] = dp[i-1][j-1] * vowels % MOD
    return sum(dp[wordLen]) % MOD

if __name__ == "__main__":  
    # wordLen = 1
    # maxVowels = 1 # Output 26
    wordLen = 4
    maxVowels = 1
    print(calculateWays(wordLen, maxVowels))
      