""" https://leetcode.com/problems/remove-invalid-parentheses/
backtracking
"""
from header import *

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        stk = []
        self.ans = set()

        def dfs(i, op):
            if i==len(s):
                if op==0: return self.ans.add(''.join(stk.copy()))
                else: return
            if op<0: return 
            # skip s[i]
            if s[i] in "()": dfs(i+1, op) 
            # choose s[i] and count non-closed parentheses
            if s[i]=='(': op += 1
            elif s[i]==')': op -= 1
            stk.append(s[i])
            dfs(i+1, op)
            stk.pop()

        
        dfs(0, 0)
        maxL = len(max(self.ans, key=len))
        return [x for x in self.ans if len(x)==maxL]
    
"""
knap sack dp
"""
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = defaultdict(set)
        
        @cache
        def dfs(st, i, op, cnt):
            if op<0:
                return
            if i==len(s):
                if op==0:
                    ans[cnt].add(st)
                return
            # skip
            dfs(st, i+1, op, cnt+1)
            # add
            if s[i]=='(':
                op += 1
            elif s[i]==')':
                op -= 1
            dfs(st+s[i], i+1, op, cnt)
            
        dfs("", 0, 0, 0)
        mn = min(ans)
        return ans[mn]