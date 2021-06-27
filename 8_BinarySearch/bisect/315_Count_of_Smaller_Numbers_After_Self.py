""" L2
bisect.insort to build binary search tree
bisect.bisect_left to find position to insert(how many nodes smaller than itself)
"""
class Solution(object):
    def countSmaller(self, nums):
        seen, ans = [], []
        for num in reversed(nums):
            bisect.insort(seen, num)
            pos = bisect.bisect_left(seen, num)
            ans.append(pos)
        return reversed(ans)