class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A = list(map(lambda a: abs(a)**2, A))
        return sorted(A)
    
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([n**2 for n in nums])
    
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        ans = []
        while l<=r:
            ls, rs = nums[l]**2, nums[r]**2
            if ls<rs:
                ans.append(rs)
                r -= 1
            else:
                ans.append(ls)
                l += 1
        return ans[::-1]