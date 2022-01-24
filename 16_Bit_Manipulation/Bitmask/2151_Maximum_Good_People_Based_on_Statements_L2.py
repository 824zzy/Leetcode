""" https://leetcode.com/problems/maximum-good-people-based-on-statements/
go over every states and check if a state is valid given the statements
"""
class Solution:
    def maximumGood(self, A: List[List[int]]) -> int:
        ans = 0
        for mask in range(1<<len(A)):
            valid = True
            for i in range(len(A)):
                if mask>>i&1 and valid:
                    for j in range(len(A)):
                        if A[i][j]!=2:
                            if A[i][j]!=mask>>j&1:
                                valid = False
                                break
            if valid: ans = max(ans, bin(mask).count('1'))
        return ans