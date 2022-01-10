""" https://leetcode.com/problems/minimum-window-substring/
use index windows and maintain a seen Counter to find answer.
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cntT = Counter(t)
        i = 0
        ans = '#'*(10**5)
        for j in range(len(s)):
            if s[j] in cntT:
                cntT[s[j]] -= 1
                while(all(v<=0 for _, v in cntT.items())):
                    ans = min(ans, s[i:j+1], key=len)
                    if s[i] in cntT: cntT[s[i]] += 1
                    i += 1
        return ans if ans!='#'*(10**5) else ''