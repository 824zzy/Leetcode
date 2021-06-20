""" L2
Use available left and right parenthesis to control dfs
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(l, r, s):
            if l==0 and r==0:
                ans.append(s)
                return
            if l>0: dfs(l-1, r+1, s+'(')
            if r>0: dfs(l, r-1, s+')')
        
        dfs(n, 0, '')
        return ans