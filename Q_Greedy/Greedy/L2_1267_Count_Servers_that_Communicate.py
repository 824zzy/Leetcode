""" https://leetcode.com/problems/count-servers-that-communicate/
learn from lee: https://leetcode.com/problems/count-servers-that-communicate/discuss/436665/Python-Simple-and-Concise
"""


class Solution:
    def countServers(self, A):
        X, Y = list(map(sum, A)), list(map(sum, zip(*A)))
        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1 and X[i] + Y[j] > 2:
                    ans += 1
        return ans
