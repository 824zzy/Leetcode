# TODO: modify this version
class FenwickTree:              # a.k.a. Binary Index Tree (BIT)
    def __init__(self, N: int):
        self.N = N
        self.arr = [0] * N
        
    def sum(self, i: int):      # i is 1-indexed
        s = 0
        while i:
            s += self.arr[i-1]
            i -= i & -i
        return s
    
    def add(self, i: int, k):   # i is 1-indexed
        while i <= self.N:
            self.arr[i-1] += k
            i += i & -i
            

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        fw = FenwickTree(N)
        bw = FenwickTree(N)
        
        r = sorted((n, i) for i, n in enumerate(rating))
        for n, i in reversed(r):
            bw.add(N-i, 1)
        
        ans = 0
        for n, i in r:
            bw.add(N-i, -1)
            a, b = fw.sum(i+1), bw.sum(N-i)
            ans += a * b + (i - a) * (N - i - b - 1)
            fw.add(i+1, 1)
        return ans