""" https://leetcode.com/problems/stickers-to-spell-word/
unbounded knapsack dp + optimization

the hardest part is to find the optimization: "if T[0] in cntS:"
"""
from header import *

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        S = [Counter(s) for s in stickers]
        
        @cache
        def dfs(T):
            if T=='':
                return 0
            # enumerate from 0 to mx
            ans = inf
            cntT = Counter(T)
            for cntS in S:
                # magic to speed up
                if T[0] in cntS:
                    _T = ''
                    for k, v in (cntT-cntS).items():
                        _T += k*v
                    ans = min(ans, 1+dfs(_T))
            return ans
        
        ans = dfs(target) 
        return ans if ans!=inf else -1

# slower solution
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        S = []
        for s in stickers:
            tmp = [0]*26
            for c in s:
                tmp[ord(c)-97] += 1
            S.append(tmp)
        T = [0]*26
        for t in target:
            T[ord(t)-97] += 1
        
        @cache
        def dfs(i, T):
            if i==len(S):
                if all(x==0 for x in T):
                    return 0
                else:
                    return inf
            # at most can choose mx stickers
            mx = 0
            for j in range(26):
                if S[i][j]:
                    mx = max(mx, ceil(T[j]/S[i][j]))
            # enumerate from 0 to mx
            ans = inf
            for n in range(mx+1):
                _T = list(T)
                for j in range(26):
                    _T[j] = max(0, T[j]-n*S[i][j])
                ans = min(ans, n+dfs(i+1, tuple(_T)))
            return ans
        
        ans = dfs(0, tuple(T)) 
        return ans if ans!=inf else -1
    
"""
["with","example","science"]
"thehat"
["notice","possible"]
"basicbasic"
["fly","me","charge","mind","bottom"]
"centorder"
["control","heart","interest","stream","sentence","soil","wonder","them","month","slip","table","miss","boat","speak","figure","no","perhaps","twenty","throw","rich","capital","save","method","store","meant","life","oil","string","song","food","am","who","fat","if","put","path","come","grow","box","great","word","object","stead","common","fresh","the","operate","where","road","mean"]
"stoodcrease"
"""