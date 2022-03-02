""" https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/
TODO: from
dba: https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/discuss/1010451/Python-2-solutions%3A-O(2n*n*log(M))-and-O(3n*k)-explained
ye15: https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/discuss/1009859/Python3-backtracking
lee215: https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/discuss/1010057/JavaPython-Binary-Search-100
"""
class Solution:
    def minimumTimeRequired(self, A, k):
        n = len(A)
        A.sort(reverse=True) # opt 1
        self.res = sum(A)
        cnt = [0] * k

        def dfs(i):
            if i == n:
                self.res = min(self.res, max(cnt))
                return
            for j in range(k):
                if cnt[j] + A[i] < self.res: # opt 3
                    cnt[j] += A[i]
                    dfs(i + 1)
                    cnt[j] -= A[i]
                if cnt[j] == 0: break # opt 2
            return False
        
        dfs(0)
        return self.res