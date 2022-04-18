""" https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/
need to be very careful about the factor pairs
1. check four paths: up+left, up+right, down_left, down+right
2. to save time, calculate the prefix sum of 2&5 factors, similar to https://leetcode.com/problems/factorial-trailing-zeroes/
3. for each path, the minimal number of factors is the number of trailing zero
"""
class Solution:
    def maxTrailingZeros(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        H = [[[0, 0] for _ in range(N+1)] for _ in range(M+1)]
        V = [[[0, 0] for _ in range(N+1)] for _ in range(M+1)]
        # horizontal and vertical prefix count of factors
        def count_factor(x):
            f2, f5 = 0, 0
            while x%2==0:
                x //= 2
                f2 += 1
            while x%5==0:
                x //= 5
                f5 += 1
            return f2, f5
            
        for i in range(M):
            for j in range(N):
                f2, f5 = count_factor(A[i][j])
                V[i+1][j+1][0] = V[i][j+1][0] + f2
                V[i+1][j+1][1] = V[i][j+1][1] + f5    
                H[i+1][j+1][0] = H[i+1][j][0] + f2
                H[i+1][j+1][1] = H[i+1][j][1] + f5
            
        ans = 0
        for i in range(M):
            for j in range(N):
                # up
                u_f2, u_f5 = V[i+1][j+1]
                # left
                l_f2, l_f5 = H[i+1][j+1]
                # center
                cur_f2, cur_f5 = V[i][j+1]
                c_f2, c_f5 = u_f2-cur_f2, u_f5-cur_f5
                # down
                dd_f2, dd_f5 = V[M][j+1]
                d_f2, d_f5 = dd_f2-u_f2, dd_f5-u_f5
                # right
                rr_f2, rr_f5 = H[i+1][N]
                r_f2, r_f5 = rr_f2-l_f2, rr_f5-l_f5
                # case 1: up left
                c1 = min(u_f2+l_f2-c_f2, u_f5+l_f5-c_f5)
                # case 2: up right
                c2 = min(u_f2+r_f2, u_f5+r_f5)
                # case 3: down left
                c3 = min(d_f2+l_f2, d_f5+l_f5)
                # case 4: down right
                c4 = min(d_f2+r_f2+c_f2, d_f5+r_f5+c_f5)
                ans = max([ans, c1, c2, c3, c4])
        return ans