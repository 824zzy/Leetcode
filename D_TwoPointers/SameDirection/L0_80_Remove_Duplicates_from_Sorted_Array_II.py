""" https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
use same direction two pointers to check if A[i-2]<A[j], then move pointer i
"""


class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        i = 0
        for j in range(len(A)):
            if i < 2 or A[i - 2] < A[j]:
                A[i] = A[j]
                i += 1
        return i


# or use Counter to compute seen element and move pointer i


class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        i = 0
        seen = Counter()

        for j in range(len(A)):
            seen[A[j]] += 1
            if seen[A[j]] <= 2:
                A[i] = A[j]
                i += 1
        return i
