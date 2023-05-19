class Solution:
    def numSplits(self, s: str) -> int:
        ans = 0
        A, B = set(), set(s)
        last = {}
        for i, c in enumerate(reversed(s)):
            if c not in last:
                last[c] = len(s)-i-1
            
        for i in range(len(s)):
            A.add(s[i])
            if s[i] in B and i==last[s[i]]:
                B.remove(s[i])
            if len(A)==len(B):
                ans += 1
        return ans

from collections import Counter, defaultdict

class Solution:
    def numSplits(self, s: str) -> int:
        ans = 0
        cnt = Counter(s)
        seen = defaultdict(int)
            
        for i in range(len(s)):
            if len(cnt.keys())==len(seen.keys()):
                ans += 1
                
            cnt[s[i]] -= 1
            if cnt[s[i]]==0: del cnt[s[i]]
            seen[s[i]] += 1
            
        return ans