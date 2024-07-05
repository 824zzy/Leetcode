""" https://leetcode.com/problems/count-palindromic-subsequences/description/
Since the length of palindromic string is 5, we can count the prefix and suffix of 0-9 in length of 1, 2.
Then we enumerate each element to count the answer while updating prefix and suffix.
"""


class Solution:
    def countPalindromes(self, A: str) -> int:
        suf = [0] * 10
        suf2 = [0] * 100
        for i in map(int, reversed(A)):
            for j, c in enumerate(suf):
                suf2[i * 10 + j] += c
            suf[i] += 1

        ans = 0
        pre = [0] * 10
        pre2 = [0] * 100
        for i in map(int, A):
            suf[i] -= 1
            for j, c in enumerate(suf):
                suf2[i * 10 + j] -= c

            ans += sum(c1 * c2 for c1, c2 in zip(pre2, suf2))

            for j, c in enumerate(pre):
                pre2[i * 10 + j] += c
            pre[i] += 1
        return ans % (10 ** 9 + 7)
