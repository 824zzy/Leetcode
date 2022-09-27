""" https://leetcode.com/problems/push-dominoes/
disgust simulation problem
"""
class Solution:
    def pushDominoes(self, A: str) -> str:
        A = 'L'+A+'R'
        A = list(A)
        r, l = 0, 0
        while r<len(A) and l<len(A):
            while l<len(A) and A[l] not in 'LR':
                l += 1
            r = l+1
            while r<len(A) and A[r] not in 'LR':
                r += 1
            
            if not(r<len(A) and l<len(A)): break
            if A[l]=='L' and A[r]=='L':
                for i in range(l+1, r):
                    A[i] = 'L'
            if A[l]=='R' and A[r]=='R':
                for i in range(l+1, r):
                    A[i] = 'R'
            if A[l]=='R' and A[r]=='L':
                if (r-l)%2:
                    for i in range(l+1, l+1+(r-l)//2):
                        A[i] = 'R'
                    for i in range(r-(r-l)//2, r):
                        A[i] = 'L'
                else:
                    for i in range(l+1, l+1+(r-l)//2-1):
                        A[i] = 'R'
                    for i in range(r-(r-l)//2+1, r):
                        A[i] = 'L'
            l = r
        return ''.join(A[1:-1])