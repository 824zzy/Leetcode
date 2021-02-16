class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.ans = []
        l = len(S)
        def dfs(S, s):
            for i, c in enumerate(S):
                if not c.isnumeric():
                    dfs(S[i+1:], s+c.lower())
                    dfs(S[i+1:], s+c.upper())
                else: s += c
            if len(s)==l: self.ans.append(s)
                
        dfs(S, '')
        return self.ans