""" https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
count the seats to find every range of plants,
then the number of ways is the multiplication of those ranges.
"""


class Solution:
    def numberOfWays(self, A: str) -> int:
        if A.count('S') & 1 or 'S' not in A:
            return 0
        ans = 1
        i = 0
        S = 0
        for j in range(len(A)):
            if A[j] == 'S':
                if S == 2:
                    ans, S = ans * (j - i), 0
                S += 1
                i = j
        return ans % (10**9 + 7)
