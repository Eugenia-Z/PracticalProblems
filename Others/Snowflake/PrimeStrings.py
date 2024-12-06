
class Solution:
  def sieve_of_eratosthenes(self, max_num):
      
    "Return a list of booleans where True means the index is a prime number"
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    for start in range(2, int(max_num ** 0.5)+1):
      if is_prime[start]:
        for multiple in range(start * start, max_num + 1, start):
          is_prime[multiple] = False
    return is_prime

  def countPrimeStrings(self, s: str) -> int:
    MOD = 1000000007
    n = len(s)

    # Step1: Precompute prime number up tp 10^6
    max_num = 10**6
    is_prime = self.sieve_of_eratosthenes(max_num)

    # Step2: Initialize the DP array
    dp = [0] *(n+1)
    dp[0] = 1 # There is one way to split an empty string

    # Step3: Interate through the string and check substrings:
    for i in range(1, n+1):
      for j in range(i):
        substring = s[j:i]
        # Check for leading zeros
        if substring[0] == '0' or len(substring) > 6:
          continue 
        num = int(substring)
        if num <= max_num and is_prime[num]:
          dp[i] = (dp[i] + dp[j]) % MOD
    return dp[n]

if __name__ == "__main__":
    s = "11375"
    sol = Solution()
    print(sol.countPrimeStrings(s))