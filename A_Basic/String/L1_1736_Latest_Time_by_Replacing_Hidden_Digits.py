""" https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/
simulate the rules
"""


class Solution:
    def maximumTime(self, time: str) -> str:
        H = list(time[:2])
        M = list(time[-2:])
        if H[0] == '?' and H[1] == '?':
            H[0], H[1] = '2', '3'
        elif H[0] == '?':
            if int(H[1]) < 4:
                H[0] = '2'
            else:
                H[0] = '1'
        elif H[1] == '?':
            if int(H[0]) == 2:
                H[1] = '3'
            else:
                H[1] = '9'

        if M[0] == '?':
            M[0] = '5'
        if M[1] == '?':
            M[1] = '9'

        return ':'.join([''.join(H), ''.join(M)])
