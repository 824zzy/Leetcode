""" https://leetcode.com/problems/push-dominoes/
disgust simulation problem
"""


class Solution:
    def pushDominoes(self, D: str) -> str:
        D = list('L' + D + 'R')
        A = [(i, x) for i, x in enumerate(D) if x in 'LR']
        for i in range(1, len(A)):
            idx_l, sign_l = A[i - 1]
            idx_r, sign_r = A[i]
            if sign_l == 'L' and sign_r == 'L':
                D[idx_l + 1:idx_r] = ['L'] * (idx_r - idx_l - 1)
            if sign_l == 'R' and sign_r == 'R':
                D[idx_l + 1:idx_r] = ['R'] * (idx_r - idx_l - 1)
            if sign_l == 'R' and sign_r == 'L':
                n = (idx_r - idx_l - 1) // 2
                D[idx_l + 1:idx_l + n + 1] = ['R'] * n
                D[idx_r - n:idx_r] = ['L'] * n
        return ''.join(D[1:-1])


"""
"RR.L"
".L.R...LR..L.."
"""
