""" https://leetcode.com/problems/kth-ancestor-of-a-tree-node/
classic algorithm: binary lifting
Binary Lifting is a technique used to find the k-th ancestor of any node in a tree in O(logn). 
This also leads to a faster algorithm in finding the lowest common ancestor (LCA) between two nodes in a tree. 
It can also be used to compute functions such as minimum, maximum and sum between two nodes of a tree in logarithmic time. 
The technique requires preprocessing the tree in O(N log N) using dynamic programming.
"""
class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        m = 1 + int(log2(n)) #at most 16 for this problem 
        self.dp = [[-1] * m for _ in range(n)] #ith node's 2^j parent
        for j in range(m):
            for i in range(n):
                if j == 0: self.dp[i][0] = parent[i] #2^0 parent
                elif self.dp[i][j-1] != -1: 
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]
    
    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0 and node != -1: 
            i = int(log2(k))
            node = self.dp[node][i]
            k -= (1 << i)
        return node 