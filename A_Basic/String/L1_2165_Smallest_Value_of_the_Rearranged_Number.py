""" https://leetcode.com/problems/smallest-value-of-the-rearranged-number/
If it's negative, simple sort reversely all digits.
If it's positive, swap the fisrt digit and the first non-zero digit.
"""


class Solution:
    def smallestNumber(self, A: int) -> int:
        S = list(map(int, str(abs(A))))
        if A > 0:
            S.sort()
            i = 0
            while S[i] == 0:
                i += 1
            S[0], S[i] = S[i], S[0]
            return int(''.join(list(map(str, S))))
        else:
            S.sort(reverse=True)
            return -1 * int(''.join(list(map(str, S))))


"""
2170596702
"""
