""" https://leetcode.com/problems/total-characters-in-string-after-transformations-i/
data structure optimized DP

dp(i, j):
1. j!=25: dp(i-1, j+1)
2. j==25: 
    1. dp(i-1, 0)
    2. dp(i-1, 1)
"""


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        A = [ord(c) - 97 for c in s]
        cnt = [0] * 26
        for x in A:
            cnt[x] += 1
        MOD = 10 ** 9 + 7
        ans = 0
        for i in range(t):
            _cnt = [0] * 26
            for j in range(26):
                if j == 25:
                    _cnt[0] = (_cnt[0] + cnt[j]) % MOD
                    _cnt[1] = (_cnt[1] + cnt[j]) % MOD
                else:
                    _cnt[j + 1] = cnt[j] % MOD
            cnt = _cnt
        return sum(cnt) % MOD


"""
a
b: 1
...
z: 25
ab: 26
bc: 27
cd: 28
...
yz: 50
zab: 51
abbc: 52
bccd: 53
...

"""
"""
"abcyy"
2
"azbk"
1
"""
