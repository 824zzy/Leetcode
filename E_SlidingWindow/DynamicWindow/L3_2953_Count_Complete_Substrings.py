""" https://leetcode.com/problems/count-complete-substrings/
enumeration + sliding window

This solution will TLE, please refer to this better one: https://leetcode.cn/problems/count-complete-substrings/solutions/2551743/bao-li-hua-chuang-mei-ju-chuang-kou-nei-31j5m/
"""
from header import *


class Solution:
    def countCompleteSubstrings(self, A: str, k: int) -> int:
        ans = 0
        for l in range(1, len(set(A)) + 1):
            mp = Counter()
            i = 0
            for j, c in enumerate(A):
                mp[A[j]] += 1
                while (
                    i < j
                    and (j and abs(ord(A[j]) - ord(A[j - 1])) > 2)
                    or len(mp) > l
                    or mp[A[j]] > k
                ):
                    mp[A[i]] -= 1
                    if mp[A[i]] == 0:
                        mp.pop(A[i])
                    i += 1
                if len(mp) == l:
                    if all(v == k for _, v in mp.items()):
                        ans += 1
        return ans


"""
"igigee"
2
"aaabbbccc"
3
"aaa"
1
"rargaa"
6
"""
