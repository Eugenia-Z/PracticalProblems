from typing import List
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        n = len(words)
        m = len(words[0])
        l = len(target)

        # Step 1: Precompute the number of times each character appears in each index
        char_count = [[0]* 26 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                char_count[j][ord(words[i][j]) - ord('a')] += 1

        # Step 2: DP array: dp[i] represents the number of ways to construct the first i characters of the target
        dp = [0] * (l+1)
        dp[0] = 1  # there is one way to form the empty prefix

        # Step 3: traverse each position in worrds and try to construct target
        for j in range(m):
        # traverse target from back to front to avoid overwriting results
            for i in range(l-1, -1, -1):
                target_char = target[i]
                target_index = ord(target_char) - ord('a')
                dp[i+1] = (dp[i+1] + dp[i] * char_count[j][target_index]) % MOD
        return dp[l]
    
if __name__ == "__main__":
    words = ["valya", "lyglb", "vldoh"]
    target = "val"
    sol = Solution()
    print(sol.numWays(words,target))