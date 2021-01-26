class Solution:
    def minimumTeachings(self, n: int, A: List[List[int]], edges: List[List[int]]) -> int:
        A = list(map(set, A))
        student = set(a for i, j in edges for a in [i, j] if not A[i - 1] & A[j - 1])
        count = collections.Counter()
        for a in student:
            count += collections.Counter(A[a - 1])
        return len(student) - max(list(count.values()) + [0])