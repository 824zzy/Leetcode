class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda x: len(x))
        dp = {}
        for w in words:
            max_len = -1
            for i in range(len(w)):
                sub = w[:i]+w[i+1:]
                max_len =  max(max_len, dp.get(sub, 0)+1)
            dp[w] = max_len
        return max(dp.values())