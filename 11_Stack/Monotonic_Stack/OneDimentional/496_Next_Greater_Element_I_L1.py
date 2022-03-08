""" https://leetcode.com/problems/next-greater-element-i/
build a next greater hash table by monotonic decreasing stask.
"""
class Solution:
    def nextGreaterElement(self, A: List[int], B: List[int]) -> List[int]:
        stk, M = [], {}
        for n in B:
            while stk and stk[-1]<n:
                M[stk.pop()] = n
            stk.append(n)
        
        return [M.get(x, -1) for x in A]
    
    
# brute force O(n^2) solution
class Solution:
    def nextGreaterElement(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        for i in range(len(A)):
            idx = B.index(A[i]) 
            for j in range(idx, len(B)):
                if B[j]>A[i]:
                    ans.append(B[j])
                    break
            else: ans.append(-1)
        return ans