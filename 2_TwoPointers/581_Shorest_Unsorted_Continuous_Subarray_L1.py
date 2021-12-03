# sort then find left and right
class Solution:
    def findUnsortedSubarray(self, A: List[int]) -> int:
        s_nums = sorted(nums)
        l, r = 0, len(nums)-1
        while l<r:
            if nums[l]==s_nums[l]: l += 1
            elif nums[r]==s_nums[r]: r -= 1
            else: break
        return r-l+1 if r-l!=0 else 0


# TODO: solution from lee215
class Solution:
    def findUnsortedSubarray(self, A: List[int]) -> int:
        reverse = filter(lambda p: p[0] > p[1], zip(l, l[1:]))
        print(reverse)
        if not reverse: return 0
        left, right = min(p[1] for p in reverse), max(p[0] for p in reverse)
        for i in xrange(len(l)):
            if l[i] > left: break
        for j in xrange(len(l)):
            if l[-j-1] < right: break
        return len(l) - j - i