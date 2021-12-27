""" Two hash table to record the edge.
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_cnt, s_cnt = Counter(t), Counter()
        i = 0
        ans = (0, float('inf'))
        for j in range(len(s)):
            s_cnt[s[j]] += 1
            while not t_cnt-s_cnt:
                s_cnt[s[i]] -= 1
                ans = min(ans, (i, j), key = lambda x: x[1]-x[0])
                i += 1
            
        return '' if ans[1]==float('inf') else s[ans[0]:ans[1]+1]