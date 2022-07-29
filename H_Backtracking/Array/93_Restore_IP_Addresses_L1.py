""" https://leetcode.com/problems/restore-ip-addresses/
dumb code but works
"""
class Solution:
    def restoreIpAddresses(self, A: str) -> List[str]:
        stk = []
        ans = set()
        
        def dfs(i):
            if i>=len(A) and len(stk)==4:
                ans.add('.'.join(stk))
                return
            for j in range(i+1, i+4):
                if 0<=i<j<len(A)+1 and 0<=int(A[i:j])<=255 and len(stk)<4 and str(int(A[i:j]))==A[i:j]:
                    stk.append(A[i:j])
                    dfs(j)
                    stk.pop()
        
        dfs(0)
        return ans