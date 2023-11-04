""" https://leetcode.com/problems/binary-trees-with-factors/
Sort the list A at first. Scan A from small element instead of index.
DP equation: dp[x] = sum(dp[y] * dp[x//y])
Time complexity: O(N^2), where N is the length of A
"""
# bottom up
class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        dp = Counter(A)
        for x in A:
            for y in A:
                if x%y==0 and x//y in dp:
                    dp[x] += dp[y]*dp[x//y]
            dp[x] %= (10**9+7)
        return sum(dp.values())%(10**9+7)

# top down
class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        @cache
        def dp(x):
            ans = 1
            for y in A:
                if x%y==0 and x//y in A:
                    ans += dp(y)*dp(x//y)
            return ans%(10**9+7)
        
        return sum(dp(x) for x in A)%(10**9+7)
            
"""
[2,4]
[2,4,5,10]
[18,3,6,2]
"""