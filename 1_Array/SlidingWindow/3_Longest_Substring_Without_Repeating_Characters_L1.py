# template
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0: return 0
        if len(s)==1: return 1
        i = 0
        ans = 0
        win = s[0]
        for j in range(1, len(s)):
            win += s[j]
            while win.count(s[i])>1 or win.count(s[j])>1:
                win = win[1:]    
                i += 1
            ans = max(ans, len(win))
        return ans