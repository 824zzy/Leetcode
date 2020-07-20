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