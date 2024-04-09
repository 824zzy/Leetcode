""" https://leetcode.com/problems/search-suggestions-system/
brute force to compare sub-strings

Time complexity: O(m*n*n) where m=len(s), n=len(P)
"""


class Solution:
    def suggestedProducts(self, P: List[str], s: str) -> List[List[str]]:
        P.sort()
        ans = []
        for i in range(1, len(s) + 1):
            sw = s[:i]
            cur = []
            for p in P:
                if p[:i] == sw and len(cur) < 3:
                    cur.append(p)
            ans.append(cur)
        return ans
