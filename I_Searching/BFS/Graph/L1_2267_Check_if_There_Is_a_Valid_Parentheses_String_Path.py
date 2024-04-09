""" https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/
count close parenthese at every dp state
"""


class Solution:
    def hasValidPath(self, A: List[List[str]]) -> bool:
        if A[0][0] == ')' or A[-1][-1] == '(':
            return False
        Q = [(0, 0, 1)]
        D = [(0, 1), (1, 0)]
        seen = {(0, 0): 1}
        while Q:
            x, y, cl = Q.pop(0)
            if x == len(A) - 1 and y == len(A[0]) - 1 and cl == 0:
                return True

            for dx, dy in D:
                if 0 <= x + dx < len(A) and 0 <= y + dy < len(A[0]):
                    if A[x + dx][y + dy] == '(':
                        ccl = cl + 1
                        if (x +
                            dx, y +
                            dy) not in seen or ccl < seen.get((x +
                                                               dx, y +
                                                               dy), -
                                                              inf):
                            seen[(x + dx, y + dy)] = ccl
                            Q.append((x + dx, y + dy, ccl))
                    else:
                        ccl = cl - 1
                        if ccl >= 0 and (
                                (x + dx, y + dy) not in seen or ccl < seen.get((x + dx, y + dy), -inf)):
                            seen[(x + dx, y + dy)] = ccl
                            Q.append((x + dx, y + dy, ccl))
        return False
