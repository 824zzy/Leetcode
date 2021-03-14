""" use hashmap to save the dp table(lee215)
Sort the list A at first. Scan A from small element to bigger.

DP equation:
dp[i] = sum(dp[j] * dp[i / j])
res = sum(dp[i])
with i, j, i / j in the list L
"""

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = {a: 1 for a in arr}
        for i, a in enumerate(dp):
            for j, b in enumerate(dp):
                if i>j and a%b==0 and a/b in dp:
                    dp[a] += dp[b]*dp[a/b]
        return sum(dp.values()) % (10**9+7)