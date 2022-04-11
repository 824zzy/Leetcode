""" https://leetcode.com/problems/implement-rand10-using-rand7/
rejection sampling
learn from lee: https://leetcode.com/problems/implement-rand10-using-rand7/discuss/151567/C%2B%2BJavaPython-1.183-Call-of-rand7-Per-rand10
"""
class Solution:
    def rand10(self):
        rand40 = 40
        while rand40 >= 40:
            rand40 = (rand7() - 1) * 7 + rand7() - 1
        return rand40 % 10 + 1