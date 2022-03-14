""" https://leetcode.com/problems/simplify-path/submissions/
simulate path rules by stack
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace('//', '/').split('/')
        stk = []
        for p in path:
            if p=='.' or not p: continue
            elif p=='..':
                if stk: stk.pop()
            else: stk.append(p)
        return '/'+'/'.join(stk)