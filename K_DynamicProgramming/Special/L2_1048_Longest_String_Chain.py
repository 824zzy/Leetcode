""" https://leetcode.com/problems/longest-string-chain/submissions/
A special dp problem:
1. Let dp(word) be the length of the longest possible word chain end at word word.
2. To calculate dp(word), we try all predecessors of word word and get the maximum length among them.

Time complexity: O(n*l*l) where n<=1000 and l<=16

Reference: https://leetcode.com/problems/longest-string-chain/discuss/1213876/Python-3-solutions-LIS-DP-Top-down-DP-Bottom-up-DP-Clean-and-Concise
"""


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        ans = 0
        dp = defaultdict(int)

        for w in words:
            dp[w] = 1
            for i in range(len(w)):
                pre = w[:i] + w[i + 1:]
                dp[w] = max(dp[w], dp[pre] + 1)
            ans = max(ans, dp[w])
        return ans


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordset = set(words)

        @cache
        def dp(word):
            ans = 1
            for i in range(len(word)):
                pre = word[:i] + word[i + 1:]
                if pre in wordset:
                    ans = max(ans, dp(pre) + 1)
            return ans

        return max(dp(w) for w in words)
