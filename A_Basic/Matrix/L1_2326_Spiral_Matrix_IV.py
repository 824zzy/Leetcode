""" https://leetcode.com/problems/spiral-matrix-iv/
the same as other spiral matrix problem, beside use linked list to store the sequence
"""


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        A = [[-1 for _ in range(n)] for _ in range(m)]
        D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        x, y = 0, 0
        dx, dy = D[d]

        while head:
            A[x][y] = head.val
            if not (0 <= x + dx < m and 0 <= y + dy < n and A[x + dx][y + dy] == -1):
                d = (d + 1) % 4
                dx, dy = D[d]
            x, y = x + dx, y + dy
            head = head.next
        return A
