""" https://leetcode.com/problems/3sum-smaller/
1. nums[i] + nums[j] + nums[k] < target ==> nums[j] + nums[k] < target - nums[i]
2. sort the array
3. two pointers to count the valid answer
"""
from header import *

# TC: O(n^2)
class Solution:
    def threeSumSmaller(self, A: List[int], t: int) -> int:
        A.sort()
        ans = 0
        for i in range(len(A)-1):
            j, k = i+1, len(A)-1
            while j<k:
                if j<k and A[j]+A[k]>=t-A[i]:
                    k -= 1
                else:
                    ans += k-j
                    j += 1
        return ans


""" https://leetcode.com/problems/3sum-smaller/
1. nums[i] + nums[j] + nums[k] < target ==> nums[k] < target - nums[i] - nums[j]
2. sort the array
3. binary search to find the k's position
"""
# TC: O(n^2*logn)
class Solution:
    def threeSumSmaller(self, A: List[int], t: int) -> int:
        A.sort()
        ans = 0
        for i in range(len(A)):
            for j in range(i+1 , len(A)):
                kx = t-A[i]-A[j]
                k = bisect_left(A, kx)
                if k>j:
                    ans += k-j-1
        return ans
                
"""
[-2,0,1,3]
2
[]
0
[0]
0
[-2,0,1,3]
1
[-2,0,1,3]
-1
[3,1,0,-2]
4
[1,1,-2]
1
"""