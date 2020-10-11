class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        dep = 0
        for c in s:
            if c=='(':
                dep += 1
                ans = max(ans, dep)
            elif c==')':
                dep -= 1
        return ans
