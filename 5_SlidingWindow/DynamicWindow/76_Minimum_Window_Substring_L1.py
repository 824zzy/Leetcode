""" https://leetcode.com/problems/minimum-window-substring/
1. use a dynamic sliding windows and a Counter to count t's frequency
2. if all Counter's frequencies are less than 0, then increase i
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0
        ans = '0'*(10**5+1)
        cnt = Counter(t)
        
        for j in range(len(s)):
            if s[j] in cnt:
                cnt[s[j]] -= 1
                while all(x<=0 for x in cnt.values()):
                    if s[i] in cnt: cnt[s[i]] += 1
                    i += 1
                    ans = min(ans, s[i-1:j+1], key=len)
        return ans if ans!='0'*(10**5+1) else ''