""" https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/
greedily count the minimum wrong positions
"""


class Solution:
    def minSwaps(self, s: str) -> int:
        ones = s.count('1')
        zeros = s.count('0')
        if abs(ones - zeros) > 1:
            return -1

        def countWrong(x):
            cnt = 0
            for i, c in enumerate(s):
                if i & 1 == 0 and c != x:
                    cnt += 1
                elif i & 1 == 1 and c == x:
                    cnt += 1
            return cnt // 2

        if ones > zeros:  # 1 in even position
            return countWrong('1')
        elif zeros > ones:  # 0 in even position
            return countWrong('0')
        else:
            return min(countWrong('1'), countWrong('0'))
