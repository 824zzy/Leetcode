""" Back-tracking
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []

        def dfs(cur_s: str, temp: List[str]) -> None:
            # Edge case
            if not cur_s:
                self.res.append(temp[:])
                return
            # for-loop
            for i in range(1, len(cur_s)+1):
                if cur_s[:i] == cur_s[:i][::-1]:
                    dfs(cur_s[i:], temp+[cur_s[:i]])

        dfs(s, [])
        return self.res