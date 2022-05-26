# Binary Lifting

Binary Lifting is a technique used to find the k-th ancestor of any node in a tree in O(logn).
This also leads to a faster algorithm in finding the lowest common ancestor (LCA) between two nodes in a tree.
It can also be used to compute functions such as minimum, maximum and sum between two nodes of a tree in logarithmic time.
The technique requires preprocessing the tree in O(N log N) using dynamic programming.

```py
"""
dp[i][j] means 2^j-th parent node of i
base case: dp[i][0]=parent[i]
dp transition: dp[i][j] = dp[ dp[i][j-1] ][j-1]

use binary representation of k to jump/lifting through dp table
"""
class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        m = 1 + int(log2(n)) # depth is at most 16 
        self.dp = [[-1] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if j == 0: self.dp[i][0] = parent[i] #2^0 parent
                elif self.dp[i][j-1] != -1: 
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]
    
    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0 and node != -1: 
            i = int(log2(k))
            node = self.dp[node][i]
            k -= (1 << i)
        return node 
```

Reference:

- [Binary Lifting with k-th ancestor and lowest common ancestor](https://iq.opengenus.org/binary-lifting-k-th-ancestor-lowest-common-ancestor)
- [Errichto tutorial](https://www.youtube.com/watch?v=oib-XsjFa-M)
