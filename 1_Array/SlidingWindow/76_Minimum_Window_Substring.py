""" L1: Template variance
use index windows and maintain a seen Counter to find answer.
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t): return ''
        
        win = []
        seen = Counter()
        thres = Counter(t)
        ans = s
        for i, c in enumerate(s):
            if c in t:
                seen[c] += 1
                win.append(i)
                # Adjust window
                while seen[s[win[0]]]>thres[s[win[0]]]:
                    seen[s[win[0]]] -= 1
                    win.pop(0)
                
                if len(thres-seen)==0 and win[-1]-win[0]<len(ans):
                    ans = s[win[0]:win[-1]+1]
        
        return '' if len(thres-seen)>0 else ans