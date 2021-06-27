""" L2
First pass: left to right, the right one will have one more candy than the left one if taller.
Second pass: right to left, the left one will be at least one more candy than the right one if taller.
"""
class Solution:
    def candy(self, A: List[int]) -> int:
        ans = [1] * len(A)
        for i in range(1, len(A)):
            if A[i]>A[i-1]: ans[i] = ans[i-1]+1
        for i in range(len(A)-1, 0, -1):
            if A[i-1]>A[i]: ans[i-1] = max(ans[i-1], ans[i]+1)
        return sum(ans)