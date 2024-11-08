""" https://leetcode.com/problems/count-special-integers/
similar to /S_Math/Combination/357_Count_Numbers_with_Unique_Digits_L2.py
the same as /S_Math/Combination/1012_Number_With_Repeated_Digits_L3.py

1. for numbers whose length is from 1 to n-1, we use the method of 357 to count numbers that have unique digits
2. for numbers whose length is n, we use dfs to count numbers that have unique digits
"""


class Solution:
    def countSpecialNumbers(self, N: int) -> int:
        def A(n, k):
            ans = 1
            for i in range(n - k + 1, n + 1):
                ans *= i
            return ans

        def dfs(i):
            if i == len(L):
                return
            for x in range(10):
                if i == 0 and x == 0:
                    continue
                if seen[x]:
                    continue
                if x < L[i]:
                    self.ans += A(9 - i, len(L) - i - 1)
                elif x == L[i]:
                    seen[x] = 1
                    dfs(i + 1)

        L = list(map(int, str(N + 1)))
        self.ans = 0
        # numbers whose length is from 1 to n-1
        for i in range(1, len(L)):
            self.ans += A(10, i) - A(9, i - 1)
        seen = [0] * 10
        # numbers whose length is n
        dfs(0)
        return self.ans
