class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = []
        def backtrack(sub, i):
            if len(sub)==len(S):
                ans.append(sub)
            else:
                if S[i].isalpha():
                    backtrack(sub+S[i].swapcase(), i+1)
                backtrack(sub+S[i], i+1)
        
        backtrack('', 0)
        return ans
    
# Bad Solution using template
class Solution(object):
    def letterCasePermutation(self, S):
        ans = []
        l = len(S)
        
        def dfs(S, sub):
            if not S and len(sub)==l:
                ans.append(sub)
            for i, c in enumerate(S):
                if c.isalpha():
                    dfs(S[i+1:], sub+c.lower())
                    dfs(S[i+1:], sub+c.upper())
                else:
                    dfs(S[i+1:], sub+c)
        
        dfs(S, '')
        return ans