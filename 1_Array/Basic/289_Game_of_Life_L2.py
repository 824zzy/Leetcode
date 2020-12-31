# Extra space solution
class Solution:
    def gameOfLife(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(A), len(A[0])
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1), (1, 1), (-1, 1)]
        modify = []
        def count(i, j):
            cnt = 0
            for d in direction:
                x, y = i + d[0], j + d[1]
                if 0<=x<M and 0<=y<N and A[x][y]: cnt += 1
            return cnt
        
        def rules(cnt, cur):
            if cur and cnt<2: return 0
            elif cur and cnt==2 or cnt==3: return 1
            elif cur and cnt>3: return 0
            elif not cur and cnt==3: return 1
            else: return cur
        
        for m in range(M):
            for n in range(N):
                cnt = count(m, n)
                val = rules(cnt, A[m][n])
                modify.append(val)
        
        for i in range(len(modify)):
            A[i//N][i%N] = modify[i]

# special flag to previent extra space
class Solution:
    def gameOfLife(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """ 
        M, N = len(A), len(A[0])
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1), (1, 1), (-1, 1)]
        modify = []
        def count(i, j):
            cnt = 0
            for d in direction:
                x, y = i + d[0], j + d[1]
                if 0<=x<M and 0<=y<N and (A[x][y]==1 or A[x][y]==2): cnt += 1
            return cnt
        
        def rules(cnt, cur):
            if cur and (cnt<2 or cnt>3): return 2
            elif not cur and cnt==3: return 3
            else: return cur
            
        
        for m in range(M):
            for n in range(N):
                cnt = count(m, n)
                A[m][n] = rules(cnt, A[m][n])
        for m in range(M):
            for n in range(N):
                A[m][n] %= 2