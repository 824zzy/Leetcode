""" https://leetcode.com/problems/minimum-window-subsequence/
top-down dp will TLE
"""
from header import *
    
# bottom-up dp
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        dp = [[inf]*(len(s2)+1) for i in range(len(s1)+1)]
        dp[0][0] = 0
        end = 0
        length = len(s1)+1
        for i in range(1, len(s1)+1):
            dp[i][0] = 0
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + dp[i - 1][j]
            if dp[i][len(s2)] < length:
                length = dp[i][len(s2)]
                end = i
        return "" if length > len(s1) else s1[end - length:end]
    
    
# greedy + binary search to simulate
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        if len(s2)==1:
            if s2[0] in s1: return s2
            else: return ''
            
        pos = defaultdict(list)
        for c2 in s2:
            if c2 in pos: continue
            for i, c1 in enumerate(s1):
                if c1==c2:
                    pos[c1].append(i)
        path = [[x] for x in pos[s2[0]]]
        
        for i in range(1, len(s2)):
            nxt_path = []
            for p in path:
                idx = bisect_right(pos[s2[i]], p[-1])
                if idx>=len(pos[s2[i]]): continue
                p.append(pos[s2[i]][idx])
                nxt_path.append(p)
            path = nxt_path
        if not path: return ''
        mn = min(path, key=lambda x: x[-1]-x[0])
        return s1[mn[0]:mn[-1]+1]
                
                
"""
"abcdebdde"
"bde"
"jmeqksfrsdcmsiwvaovztaqenprpvnbstl"
"u"
"abcdebde"
"bde"
"wcbsuiyzacfgrqsqsnodwmxzkz"
"xwqe"
"jmeqksfrsdcmsiwvaovztaqenprpvnbstl"
"k"
"cnhczmccqouqadqtmjjzl"
"mm"
"""