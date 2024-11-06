""" https://leetcode.com/problems/string-compression-iii/
string simulation
"""


class Solution:
    def compressedString(self, A: str) -> str:
        A += "*"
        ans = ""
        cnt = 0
        for j in range(len(A)):
            if j and A[j] != A[j - 1]:
                x, y = divmod(cnt, 9)
                ans += ("9" + A[j - 1]) * x if x else ""
                ans += (str(y) + A[j - 1]) if y else ""
                cnt = 0
            cnt += 1
        return ans
