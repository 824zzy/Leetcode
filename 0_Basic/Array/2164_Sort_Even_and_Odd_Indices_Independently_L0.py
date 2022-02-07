""" https://leetcode.com/problems/sort-even-and-odd-indices-independently/
"""
class Solution:
    def sortEvenOdd(self, A: List[int]) -> List[int]:
        A[::2], A[1::2] = sorted(A[::2]), sorted(A[1::2])[::-1]
        return A
    
# readable solution
class Solution:
    def sortEvenOdd(self, A: List[int]) -> List[int]:
        o, e = [], []
        for i in range(len(A)):
            if i&1==0: o.append(A[i])
            else: e.append(A[i])
        
        o.sort()
        e.sort(reverse=True)
        
        ans = []
        for i in range(len(e)):
            ans.append(o[i])
            ans.append(e[i])
        return ans+[o[-1]] if len(A)&1==1 else ans