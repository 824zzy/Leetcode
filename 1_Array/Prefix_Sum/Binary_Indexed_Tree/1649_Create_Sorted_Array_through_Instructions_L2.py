class Solution:
    def createSortedArray(self, A: List[int]) -> int:
#         def search_idx(nums, target):
#             left=0
#             right=len(nums)-1
#             while left<=right:
#                 mid=(left+right)//2
#                 if (nums[mid]>=target):
#                     right=mid-1
#                 else:
#                     left=mid+1
#             l = sum([1 for i in range(left) if nums[i]<target])
#             r = sum([1 for i in range(left, len(nums)) if nums[i]>target])
#             self.arr.insert(left, target)
#             return min(l, r)
                
        
#         ans = 0
#         self.arr = []
#         for i in instructions:
#             ans += search_idx(self.arr, i)
#         return ans
        m = max(A)
        c = [0] * (m + 1)
        
        def update(x):
            while (x <= m):
                c[x] += 1
                x += x & -x

        def get(x):
            res = 0
            while (x > 0):
                res += c[x]
                x -= x & -x
            return res

        res = 0
        for i, a in enumerate(A):
            res += min(get(a - 1), i - get(a))
            update(a)
        return res % (10**9 + 7)
