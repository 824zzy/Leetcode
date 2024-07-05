""" L1
simple usage of two pointer
"""
# in-place solution


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i, j = 0, 1
        while i < len(A) and j < len(A):
            if A[i] % 2 == 1 and A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
            elif A[i] % 2 == 0:
                i += 2
            elif A[j] % 2 == 1:
                j += 2
        return A


# straight-forward solution


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd, even = [], []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])
        ans = []
        for i in range(len(odd)):
            ans.append(even[i])
            ans.append(odd[i])
        return ans
