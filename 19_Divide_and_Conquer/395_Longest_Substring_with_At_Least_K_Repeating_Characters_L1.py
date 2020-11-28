class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dfs(s):
            if len(s)<k:
                return 0
            spliter = [c for c, v in Counter(s).items() if v<k]
            for sp in spliter:
                return max(dfs(sub) for sub in s.split(sp))
            return len(s)
        return dfs(s)