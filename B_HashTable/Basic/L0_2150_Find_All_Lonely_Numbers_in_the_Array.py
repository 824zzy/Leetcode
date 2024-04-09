""" https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/
find Counter elements which appear once and lonely
"""


class Solution:
    def findLonely(self, A: List[int]) -> List[int]:
        cnt = Counter(A)
        ans = []
        for k, v in cnt.items():
            if v == 1 and k - 1 not in cnt and k + 1 not in cnt:
                ans.append(k)
        return ans
