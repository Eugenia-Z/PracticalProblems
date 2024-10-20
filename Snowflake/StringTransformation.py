class Solution:
    def getNumWays(self, src: str, target: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(src)
        
        # Check if target is a rotation of src
        combines = src + src  # concatenation to check for rotations
        if target not in combines:
            return 0
        
        # Find the number of steps to transform src to target (different shifts/rotations)
        rotations = []  # List to store all valid rotations
        for i in range(1, n):
            if src[i:] + src[:i] == target:
                rotations.append(i)
        
        if not rotations and src != target:
            return 0
        
        # DP array to count the number of ways to transform in k steps
        dp = [[0] * n for _ in range(k + 1)]
        dp[0][0] = 1  # Initially, the string is in its original form
        
        # Iterate through each step
        for step in range(1, k + 1):
            for i in range(n):  # For each position of src
                for r in rotations:  # For each valid rotation
                    dp[step][(i + r) % n] = (dp[step][(i + r) % n] + dp[step - 1][i]) % MOD
        
        return dp[k][0]  # We want to end up at position 0 (which is target)
    
if __name__ == "__main__":
    src = "ababab"
    target = "ababab"
    k = 1
    sol = Solution()
    print(sol.getNumWays(src, target, k))
