""" https://leetcode.com/problems/move-pieces-to-obtain-a-string/
777, 2337 are the same.

Use two pointers to check if every pair of "L" and "R" is valid,
or form pairs first and then check if every pair is valid.
"""


class Solution:
    def canChange(self, S: str, T: str) -> bool:
        i, j = 0, 0
        while i < len(S) and j < len(T):
            while i < len(S) and S[i] == '_':
                i += 1
            while j < len(T) and T[j] == '_':
                j += 1
            if i == len(S) or j == len(T):
                break
            if S[i] == T[j] == 'L':
                if i < j:
                    return False
            elif S[i] == T[j] == 'R':
                if i > j:
                    return False
            else:
                return False
            i, j = i + 1, j + 1
        return 'L' not in S[i:] and 'R' not in S[i:
                                                 ] and 'L' not in T[j:] and 'R' not in T[j:]


# or form pairs first and then check if every pair is valid
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        S = []
        for i in range(len(start)):
            if start[i] == 'L':
                S.append((i, 'L'))
            elif start[i] == 'R':
                S.append((i, 'R'))

        T = []
        for i in range(len(target)):
            if target[i] == 'L':
                T.append((i, 'L'))
            elif target[i] == 'R':
                T.append((i, 'R'))

        if len(S) != len(T):
            return False
        for (s, si), (t, ti) in zip(S, T):
            if si == ti == 'L':
                if s < t:
                    return False
            elif si == ti == 'R':
                if s > t:
                    return False
            else:
                return False
        return True
