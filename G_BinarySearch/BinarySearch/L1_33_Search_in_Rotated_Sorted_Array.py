""" https://leetcode.com/problems/search-in-rotated-sorted-array/
Two approaches:

Solution 1 (one-pass, binary search + categorization):
At each step, decide whether t lies in the "good" half by checking which side
is sorted and whether t falls inside that sorted range. Tighter but trickier.

There are two cases that can lead to r=m:
1. When the left part is sorted and t is in the range of [A[l], A[m]].
2. When there is a twist in the left part and t is in the left part,
   i.e., A[l]<=t or t<=A[m].

Solution 2 (two-pass, easier to reason about):
1. Binary search for the pivot (index of the smallest element).
2. Bisect the sorted half that contains t. Same O(log n) but two clean passes.
"""


class Solution:
    def search(self, A: List[int], t: int) -> int:
        def fn(m):
            if A[l] <= A[m]:  # if left part is ordered
                # if t in left part
                if A[l] <= t <= A[m]:
                    return True
                else:
                    return False
            elif A[l] <= t or t <= A[m]:  # [6]70[1]
                return True

            if A[m] <= A[r]:  # if right part is ordered
                # if t in right part
                if A[m] <= t <= A[r]:
                    return False
                else:
                    return True
            elif A[m] <= t or t <= A[r]:  # [6]70[1]
                return False

        l, r = 0, len(A) - 1
        while l < r:
            m = (l + r) // 2
            if fn(m):
                r = m
            else:
                l = m + 1
        return l if l < len(A) and A[l] == t else -1


class Solution2:
    def search(self, A: List[int], t: int) -> int:
        n = len(A)
        # 1. find pivot (index of smallest element) via binary search
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if A[m] > A[r]:
                l = m + 1
            else:
                r = m
        pivot = l
        # 2. pick the sorted half that contains t, then bisect
        if pivot and A[0] <= t <= A[pivot - 1]:
            i = bisect_left(A, t, 0, pivot)
        else:
            i = bisect_left(A, t, pivot, n)
        return i if i < n and A[i] == t else -1
