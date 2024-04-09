""" https://leetcode.com/problems/replace-elements-in-an-array/
create a map from value to index and update it through operations
"""


class Solution:
    def arrayChange(self, A: List[int],
                    operations: List[List[int]]) -> List[int]:
        mp = {x: i for i, x in enumerate(A)}
        for x, y in operations:
            mp[y] = mp[x]
            mp.pop(x)

        ans = [0] * len(A)
        for k, v in mp.items():
            ans[v] = k
        return ans
