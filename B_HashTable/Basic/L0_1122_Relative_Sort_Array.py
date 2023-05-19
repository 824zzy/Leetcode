""" https://leetcode.com/problems/relative-sort-array/
1. sort the elements of A that relative ordering of items in B
2. sort remained elements of A and place them at the end of ans
"""
class Solution:
    def relativeSortArray(self, A: List[int], B: List[int]) -> List[int]:
        cnt = Counter(A)
        ans = []
        # sort the elements of A that relative ordering of items in B
        for x in B: 
            ans.extend([x]*cnt[x])
            cnt.pop(x)
        # sort remained elements of A and place them at the end of ans
        cnt = sorted(cnt.items())
        for k, v in cnt:
            ans.extend([k]*v)
        return ans