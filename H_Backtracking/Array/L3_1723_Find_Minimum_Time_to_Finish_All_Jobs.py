""" https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/
The same as 2305, backtracking with pruning: https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/discuss/1010057/JavaPython-Binary-Search-100

Optimization 1:
we assign the most time consuming job first.

Optimization 2:
Assign a job to totally free worker only once.

Optimization 3:
Update the res and don't go forward if work load already >= result

Time complexity: O(k^n)
"""


class Solution:
    def minimumTimeRequired(self, A, k):
        n = len(A)
        A.sort(reverse=True)  # optimization 1
        self.ans = sum(A)
        cnt = [0] * k

        def dfs(i):
            if i == n:
                self.ans = min(self.ans, max(cnt))
                return
            for j in range(k):
                if cnt[j] + A[i] < self.ans:  # optimization 3
                    cnt[j] += A[i]
                    dfs(i + 1)
                    cnt[j] -= A[i]
                if cnt[j] == 0:
                    break  # optimization 2
            return False

        dfs(0)
        return self.ans
