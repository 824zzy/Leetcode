""" L0
compare sub-strings
"""
class Solution:
    def suggestedProducts(self, P: List[str], s: str) -> List[List[str]]:
        P.sort()
        ans = []
        for i in range(1, len(s)+1):
            sw = s[:i]
            cur = []
            for p in P:
                if p[:i]==sw and len(cur)<3: cur.append(p)
            ans.append(cur)
        return ans