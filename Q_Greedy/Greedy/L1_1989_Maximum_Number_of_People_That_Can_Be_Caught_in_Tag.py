""" https://leetcode.com/problems/maximum-number-of-people-that-can-be-caught-in-tag/
for each "it":
1. find the right most "non-it"
2. go its left until dist or previous right most
"""
from header import *


class Solution:
    def catchMaximumAmountofPeople(self, A: List[int], d: int) -> int:
        ans = 0
        right_most = 0
        for i in range(len(A)):
            # if it is a "it"
            if A[i] == 1:
                # go left
                for j in range(max(i - d, right_most), i):
                    right_most = max(right_most, j + 1)
                    if A[j] == 0:
                        ans += 1
                        break
                else:
                    # go right
                    for j in range(max(i + 1, right_most),
                                   min(i + d + 1, len(A))):
                        right_most = max(right_most, j + 1)
                        if A[j] == 0:
                            ans += 1
                            break
                # print(i, "|", right_most, ans)
        return ans


"""
[0,1,0,1,0]
3
[1]
1
[0]
1
[1,1,0,1,0,1]
2
[0,1,1,0,0,1,0,1,1]
4
"""
