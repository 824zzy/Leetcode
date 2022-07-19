""" https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/
Translate the problem to: rearrange projects to ensure no two adjacent projects are the same. So there are only two scenarios:
1. if most frequent projects less or equal than half total projects, all the projects can be done
    a_a_a_a_a and bbccdd => abacabadadc
2. if most frequent projects more than half total projects, only (sm-mx)*2+1 can be done
    a_a_a_a_a and bcd => abacadaa
"""
class Solution:
    def numberOfWeeks(self, A: List[int]) -> int:
        sm = sum(A)
        mx = max(A)
        if mx<=sm/2: return sm
        else: return (sm-mx)*2+1