""" https://leetcode.com/problems/remove-invalid-parentheses/
1. Generate all valid parentheses from string s, we can memoize them to avoid re-compute sub-problem again. It's the same idea with 140. Word Break II.
2. Then get the maximum length among those valid parentheses.
3. Filter the result by choosing parentheses which has the length equals to the maximum length.
https://leetcode.com/problems/remove-invalid-parentheses/discuss/606847/JavaPython-DFS-with-Memoization-Fastest-Clean-and-Concise
"""
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