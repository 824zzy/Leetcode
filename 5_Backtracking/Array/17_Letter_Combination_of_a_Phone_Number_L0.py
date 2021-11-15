""" https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/445658/Python3-multiple-implementations-(96.33)
"""
class Solution:
    def letterCombinations(self, D: str) -> List[str]:
        M = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
        
        ans = []
        stk = []
        def dfs(d):
            if not d: return ans.append("".join(stk.copy()))
            for k in M[d[0]]: 
                stk.append(k)
                dfs(d[1:])
                stk.pop()
        
        if D: dfs(D)
        return ans

# dfs with state 
class Solution:
    def letterCombinations(self, D: str) -> List[str]:
        M = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
        
        self.ans = []
        def dfs(comb, d):
            if not d:
                self.ans.append(comb)
                return 
            for k in M[d[0]]: dfs(comb+k, d[1:])
        
        if D: dfs('', D)
        return self.ans