""" https://leetcode.com/problems/calculate-money-in-leetcode-bank/
For example, a refers to first two rows, b refers to last row. Use arithmetic progression to calculate the sum of each row.
1 2 3 4 5 6 7
2 3 4 5 6 7 8
3 4 5
"""


class Solution:
    def totalMoney(self, n: int) -> int:
        x, r = divmod(n, 7)
        a = 28 * x + x * (x - 1) * 7 // 2
        b = (x + 1) * r + (r - 1) * r // 2
        return a + b


# simulation solution
class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        x = 1
        for i in range(1, n + 1):
            ans += x
            x += 1
            if i % 7 == 0:
                x -= 6
        return ans


"""
510
20
30
50
100
500
"""
