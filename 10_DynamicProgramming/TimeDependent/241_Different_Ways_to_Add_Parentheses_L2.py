""" https://leetcode.com/problems/different-ways-to-add-parentheses/
https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/764006/Python3-dp
"""
class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        ops = {
            "-": lambda x, y: x - y,
            "+": lambda x, y: x + y,
            "*": lambda x, y: x * y,
        }
        
        @cache
        def dfs(l, r):
            ans = []
            for i in range(l, r):
                if s[i] in ops:
                    ans += [ops[s[i]](le, ri) for le in dfs(l, i) for ri in dfs(i+1, r)]
            
            return ans if len(ans) != 0 else [int(s[l:r])]
        
        return dfs(0, len(s))