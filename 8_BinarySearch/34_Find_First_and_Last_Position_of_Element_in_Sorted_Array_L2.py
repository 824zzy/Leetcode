# Binary Search
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binSearch(l, h, t):
            while l<=h:
                m = (l+h)//2
                if nums[m]==t:
                    return m
                elif nums[m]>t:
                    h = m - 1
                else:
                    l = m + 1
            return l
            
        l, h = binSearch(0, len(nums)-1, target-0.5), binSearch(0, len(nums)-1, target+0.5)-1
        if l<=h: return [l, h]
        else: return [-1, -1]

# Using groupby
class Solution:
    def searchRange(self, A: List[int], t: int) -> List[int]:
        if t not in A: return [-1, -1]
        A = [[c, len(list(s))] for c, s in itertools.groupby(A)]
        ans = 0
        for c, l in A:
            if c==t: return [ans, ans+l-1]
            else: ans += l