""" L1: https://leetcode.com/problems/generate-parentheses/submissions/
Use available left and right parenthesis to control backtracking
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stk = []
        def dfs(l, r):
            if l==r and r==0: return ans.append(''.join(stk.copy())) 
            if l>0:
                stk.append('(')
                dfs(l-1, r+1)
                stk.pop()
            if r>0:
                stk.append(')')
                dfs(l, r-1)
                stk.pop()
            
        dfs(n, 0)
        return ans
    
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