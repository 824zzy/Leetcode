""" https://leetcode.com/problems/confusing-number/
implementation
"""


class Solution:
    def confusingNumber(self, n: int) -> bool:
        new = []
        for x in reversed(str(n)):
            if x in '23457':
                return False
            if x == '6':
                new.append('9')
            elif x == '9':
                new.append('6')
            else:
                new.append(x)
        return int(''.join(new)) != n
