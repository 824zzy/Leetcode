""" L2: https://leetcode.com/problems/can-make-palindrome-from-substring/
TODO: https://leetcode.com/problems/can-make-palindrome-from-substring/discuss/1201798/Python3-prefix-freq
why 2*k+1?
"""


class Solution:
    def canMakePaliQueries(
            self, s: str, queries: List[List[int]]) -> List[bool]:
        prefix = [[0] * 26]
        for c in s:
            elem = prefix[-1].copy()
            elem[ord(c) - 97] += 1
            prefix.append(elem)

        ans = []
        for left, right, k in queries:
            cnt = sum(1 & (prefix[right + 1][i] - prefix[left][i])
                      for i in range(26))
            ans.append(cnt <= 2 * k + 1)
        return ans
