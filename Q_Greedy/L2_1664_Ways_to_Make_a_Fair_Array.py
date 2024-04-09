""" Explain from lee215
We will split the array into two parts, left and right.
Firstly we count the sum to an array right,
where right[0] = A[0] + A[2] +...
and right[1] = A[1] + A[3] +...

Now we iterates the whole array A, and try to split at each A[i].
When move one element from right to left,
we reduce the sum in right,
check the if it's fair,
then increse the sum in left.
"""


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        s1 = [0, 0]
        s2 = [sum(nums[0::2]), sum(nums[1::2])]
        ans = 0
        for i, n in enumerate(nums):
            s2[i % 2] -= n
            if s1[0] + s2[1] == s1[1] + s2[0]:
                ans += 1
            s1[i % 2] += n
        return ans
